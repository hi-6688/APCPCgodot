# Project Maintenance Rules

## 1. Context Awareness (上下文感知)
- Always read @[README.md] at the start of a task to understand the current project status.
- Before editing files, check the project structure in README.md to ensure consistency.

## 2. Documentation Updates (文檔更新)
- Update @[README.md] whenever a feature is completed, a new file is created, or a major change is made.
- **Strict Adherence**: When updating README.md, you MUST follow the "Standard Structure" defined below.

## 3. README Standard Structure (標準格式)
The README.md must strictly follow this structure and language requirement (Traditional Chinese):

### I. 專案標題與簡介
   - Title: # Project Name (開發筆記)
   - Content: Brief description of tech stack (Godot + FastAPI + Docker).

### II. 🛠️ 技術堆疊 (Tech Stack)
   - Frontend: Godot 4 (WebSocketPeer)
   - Backend: Python FastAPI + SQLModel (PostgreSQL/SQLite)
   - Infrastructure: Docker, Docker Compose, DigitalOcean App Platform

### III. 📁 檔案結構全覽 (Project File Structure)
   - Must list **ALL** files and folders (including .env, Dockerfile, docker-compose.yml, app.yaml).
   - Use 	ree diagram format.
   - **Crucial**: Every file MUST have a comment explaining its purpose.

### IV. 🚀 環境與執行 (Quick Start - Docker First)
   - Provide copy-paste ready terminal commands for **Docker Deployment**.
   - Standard Command: docker-compose up --build
   - State the "Success Signal" (e.g., Uvicorn running on 0.0.0.0:8080).

### V. 📡 通訊協議 (Protocol)
   - Define WebSocket URLs and JSON formats.

### VI. 📝 開發進度 (Dev Log)
   - Keep a checklist of Completed (-[x]) and Todo (-[ ]) items.
