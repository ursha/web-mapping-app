from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
from fastapi.responses import JSONResponse
from database import list_duckdb_tables, query_duckdb_table_as_geojson
# Load environment variables
load_dotenv()

# ✅ Define the app first
app = FastAPI()

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://0.0.0.0:8000"] if you want to be strict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Other routes (optional)
@app.get("/ping")
def ping():
    return {"status": "OK"}

@app.get("/config/mapbox-token")
def get_token():
    return {"token": os.getenv("MAPBOX_TOKEN")}



####query duckdb 
@app.get("/api/tables", response_class=JSONResponse)
def get_tables():
    tables = list_duckdb_tables()
    return {"tables": tables}

@app.get("/api/table-geojson/{table_name}", response_class=JSONResponse)
def get_table_geojson(table_name: str):
    try:
        geojson = query_duckdb_table_as_geojson(table_name)
        return geojson
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))





# Mount frontend (optional)
app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")


