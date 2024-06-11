from fastapi import FastAPI

app = FastAPI()


@app.get("/") # Runs on port 8000
async def root():
    return {"message": "Hello World"}