# Web Mapping App – UI Development Plan

## ✅ Task Checklist

### 🧱 General Setup
- [x] Create HTML structure with `#map` container
- [x] Link Mapbox GL JS CSS and JS via CDN
- [x] Add CSS to style the map container

### 🗺️ Map Initialization
- [x] Initialize Mapbox map (token, center, zoom, style)
- [x] Add map navigation controls (zoom, rotation)

### 🗂️ Layer Management
- [ ] Add base map layers (streets, satellite, etc.)
- [ ] Add GeoServer WMS layer using getCapabilities
- [ ] Add toggle controls for layers (checkboxes/buttons)

### 🧩 Interactivity
- [ ] Display popup on click (feature attributes)
- [ ] Highlight feature on hover
- [ ] Add draw tool to select areas (Mapbox GL Draw)
- [ ] Add search/filter form (query API and zoom to results)

### 🔁 Data Integration
- [ ] Fetch GeoJSON data from FastAPI
- [ ] Display fetched data on the map (new source/layer)

### 🖥️ User Interface
- [ ] Design responsive UI layout (map + side panel/nav)
- [ ] Add legend panel (dynamic layer legend)
- [ ] Add loading spinner while fetching data
- [ ] Implement layer visibility toggles

### 🔐 User Authentication
- [ ] Add login form (HTML + JS)
- [ ] Store JWT token in localStorage
- [ ] Attach token to API calls (Authorization header)
- [ ] Protect selected FastAPI routes
- [ ] Restrict access to vector tiles if needed

### 🧱 Backend & API
- [x] Create FastAPI project with `/config/mapbox-token`
- [ ] Add `/features` endpoint for GeoJSON
- [ ] Add `/login`, `/register`, and `/me` endpoints
- [ ] Add `/tilejson.json` for PMTiles metadata
- [ ] Serve static frontend from backend (`StaticFiles`)
- [ ] Add `/h3-cells` API to return hexagons intersecting a bbox or polygon

### 🗄️ Database (PostgreSQL + PostGIS)
- [ ] Install PostGIS
- [ ] Create spatial tables for layers
- [ ] Add indexes on geometry columns
- [ ] Create views or materialized views for tile serving

### 🌐 Tile Infrastructure
- [ ] Add Martin server to serve vector tiles from PostGIS
- [ ] Configure Martin with `config.toml`
- [ ] Test Martin vector tiles via `/tiles/{z}/{x}/{y}.pbf`
- [ ] Add TileServer GL for raster + vector style hosting
- [ ] Integrate PMTiles and serve `.pmtiles` via TileServer
- [ ] Display PMTiles via Mapbox GL JS with vector source

### 🔷 H3 Hexagon Integration
- [ ] Install `h3-py` Python library
- [ ] Generate H3 hexagons from bbox or polygon on the backend
- [ ] Serve hexagons as GeoJSON via FastAPI
- [ ] Add layer to frontend map to visualize H3 cells
- [ ] Optional: store H3 cells in DuckDB/PostGIS for analysis

### 🦆 DuckDB Integration
- [ ] Set up DuckDB with Python (`duckdb` package)
- [ ] Load GeoParquet or CSV files into DuckDB
- [ ] Run spatial queries using `ST_Intersects`, H3 functions, etc.
- [ ] Create FastAPI endpoints to query DuckDB and return results

---

## 🚀 Running the App Locally

### 1. Start the FastAPI Backend

```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload --port 8001

### 2. Start the mapbox map 
python3 -m http.server 8000