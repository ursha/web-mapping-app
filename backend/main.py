from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

# Load .env from backend directory
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# ✅ Apply CORS middleware immediately after app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TEMP: Allow all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Test endpoint
@app.get("/ping")
def ping():
    return {"status": "OK"}

# ✅ Token endpoint
@app.get("/config/mapbox-token")
def get_token():
    return {"token": os.getenv("MAPBOX_TOKEN")}

# ✅ Serve frontend (place this LAST!)
app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")
