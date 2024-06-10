# Hackathon Hub, FastAPI Based Tron Game backend
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
    

class Player:
    def __init__(self, name, score, direction):
        self.name = name
        self.direction = direction
        self.score = score

    def handle_input(self, direction):
        if direction in ["N", "E", "S", "W"]:
            self.direction = direction
        else:
            print("Invalid direction input")


app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    player = Player(name="Player1", score=0, direction="N")
    try:
        while True:
            data = await websocket.receive_text()
            player.handle_input(data)  # Update player direction
            await websocket.send_text(f"Direction set to: {player.direction}")
    except WebSocketDisconnect as e:
        print(f"Client disconnected: {e}")
