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

### 🔐 User Authentication (Optional)
- [ ] Add login form (HTML + JS)
- [ ] Store JWT token in localStorage
- [ ] Attach token to API calls (Authorization header)

---

> To mark a task complete, just change `[ ]` to `[x]`.


## 🚀 Running the App Locally

### 1. Start the FastAPI Backend

```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload --port 8001


cd frontend
python3 -m http.server 8000 --bind 0.0.0.0
