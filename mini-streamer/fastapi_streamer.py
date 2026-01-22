from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

async def video_streamer():
    for i in range(20):
        yield b"fake video bytes for the streamer"

@app.get('/')
async def main():
    return StreamingResponse(video_streamer())