# X-Misz OS

Lightweight server management OS and control panel for low-resource ARM servers.

## Overview

X-Misz OS adalah project operating environment dan control panel ringan untuk mengelola server berbasis ARM64 dengan sumber daya terbatas.

Project ini dirancang untuk menyediakan antarmuka web sederhana untuk memantau dan mengelola sistem server, Docker container, storage, network, dan aplikasi self-hosted.

## Goals

- Lightweight dan hemat resource
- Mendukung perangkat ARM64
- Cocok untuk mini server dan single-board computer
- Monitoring sistem secara real-time
- Manajemen Docker container
- Antarmuka web yang sederhana dan responsif
- Cocok untuk homelab, learning, dan self-hosted services

## Current Environment

Project saat ini dikembangkan dan diuji pada:

| Component | Specification |
|---|---|
| Device | HG680P |
| SoC | Amlogic S905X |
| Architecture | ARM64 / aarch64 |
| RAM | 2 GB |
| Internal Storage | Approximately 7.3 GB eMMC |
| Operating System | Armbian |
| Container Runtime | Docker |
| API Port | 8080 |

## Tech Stack

- Armbian Linux
- Docker
- Python
- FastAPI
- Uvicorn
- Vanilla HTML, CSS, and JavaScript
- psutil
- Docker SDK for Python

## Current Features

### System API

Available API endpoints:

```text
GET /api
GET /api/health
GET /api/system
GET /api/docker
