# test_websocket.py

import pytest
import websockets
import asyncio

@pytest.mark.asyncio
async def test_websocket():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send("N")
        response = await websocket.recv()
        assert response == "Direction set to: N"

        await websocket.send("E")
        response = await websocket.recv()
        assert response == "Direction set to: E"

        await websocket.send("S")
        response = await websocket.recv()
        assert response == "Direction set to: S"

        await websocket.send("W")
        response = await websocket.recv()
        assert response == "Direction set to: W"

# Run the tests
if __name__ == "__main__":
    asyncio.run(test_websocket())
