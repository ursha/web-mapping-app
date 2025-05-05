# Web Mapping App – UI Development Plan

## ✅ Task Checklist

### 🧱 General Setup
- [ ] Create HTML structure with `#map` container
- [ ] Link Mapbox GL JS CSS and JS via CDN
- [ ] Add CSS to style the map container

### 🗺️ Map Initialization
- [ ] Initialize Mapbox map (token, center, zoom, style)
- [ ] Add map navigation controls (zoom, rotation)

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
