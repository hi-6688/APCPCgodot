import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from sqlmodel import Session
from database import create_db_and_tables, engine, GameRoom

# 設定 Logging (12-Factor: Logs as Event Streams)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Lifespan: 處理啟動與關閉 (12-Factor: Disposability)
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Server starting up...")
    create_db_and_tables()
    yield
    logger.info("Server shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Health Check Endpoint (For DigitalOcean Load Balancer)
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, token: str = None):
    await websocket.accept()
    
    # 驗證房間與 Token (12-Factor: Backend Logic)
    with Session(engine) as session:
        room = session.get(GameRoom, room_id)
        
        if not room:
            logger.warning(f"Connection failed: Invalid Room ID {room_id}")
            await websocket.close(code=4000, reason="Invalid Room ID")
            return
            
        # 驗證身份 (Host vs Guest)
        is_host = (token == room.host_token)
        is_guest = (token == room.guest_token)
        
        if not is_host and not is_guest:
             # 如果是 Guest 還沒加入，且目前沒有 Guest，則嘗試註冊為 Guest (如果是這樣設計的話)
             # 但目前看來 bot.py 只生成了 host_token。
             # 簡單起見，我們暫時只允許 Host 連線，或是之後再擴充 Guest 邏輯
             logger.warning(f"Connection failed: Invalid Token for Room {room_id}")
             await websocket.close(code=4001, reason="Invalid Token")
             return

    logger.info(f"玩家成功連線！Room: {room_id}, IsHost: {is_host}")
    
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f"[{room_id}] Received: {data}")
            await websocket.send_json({"status": "received", "room": room_id})
    except WebSocketDisconnect:
        logger.info(f"[{room_id}] 玩家斷線")
