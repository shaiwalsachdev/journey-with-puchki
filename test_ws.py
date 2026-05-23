import asyncio
import websockets

async def test():
    async with websockets.connect("ws://127.0.0.1:8000/ws/voice-chat") as ws:
        # Wait for the backend to connect to Gemini and wait for input
        print("Connected!")
        try:
            msg = await ws.recv()
            print("Received:", msg)
        except Exception as e:
            print("Error:", e)

asyncio.run(test())
