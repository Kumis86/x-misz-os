from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import os
import platform
import socket
import time

import psutil
import docker


# =========================================================
# X-Misz OS Configuration
# =========================================================

APP_NAME = "X-Misz OS"
APP_VERSION = "0.1.0"

BASE_DIR = "/opt/x-misz-os"
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


# =========================================================
# FastAPI Application
# =========================================================

app = FastAPI(
    title=f"{APP_NAME} API",
    version=APP_VERSION,
    description="Lightweight server management API for X-Misz OS",
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# Docker
# =========================================================

def get_docker_client():

    try:
        return docker.from_env()

    except Exception:
        return None


# =========================================================
# API
# =========================================================

@app.get("/api")
def api_root():

    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "status": "online",
    }


@app.get("/api/health")
def health():

    return {
        "status": "ok",
        "hostname": socket.gethostname(),
        "uptime": int(time.time() - psutil.boot_time()),
    }


@app.get("/api/system")
def system_info():

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {

        "hostname": socket.gethostname(),

        "platform": platform.platform(),

        "architecture": platform.machine(),

        "kernel": platform.release(),

        "cpu": {
            "usage": psutil.cpu_percent(interval=0.5),
            "cores": psutil.cpu_count(),
        },

        "memory": {
            "total": memory.total,
            "used": memory.used,
            "available": memory.available,
            "percent": memory.percent,
        },

        "disk": {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent,
        },

        "uptime": int(time.time() - psutil.boot_time()),
    }


@app.get("/api/docker")
def docker_info():

    client = get_docker_client()

    if client is None:

        return {
            "available": False,
            "containers": [],
        }


    containers = []


    for container in client.containers.list(all=True):

        image = (
            container.image.tags[0]
            if container.image.tags
            else container.image.short_id
        )


        containers.append({

            "id": container.short_id,

            "name": container.name,

            "status": container.status,

            "image": image,

        })


    return {

        "available": True,

        "containers": containers,

    }


# =========================================================
# Frontend
# =========================================================

if os.path.isdir(FRONTEND_DIR):

    app.mount(
        "/",
        StaticFiles(
            directory=FRONTEND_DIR,
            html=True,
        ),
        name="frontend",
    )
