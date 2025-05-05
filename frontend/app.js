mapboxgl.accessToken = 'pk.eyJ1IjoiYXRhaXAiLCJhIjoiY21hYXU0aWhpMDhuaTJqc2N3ZzN0dWs2NyJ9.tXPV5QBlOGVW7FOzLkzm4A';

const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [-0.12, 51.5], // London
  zoom: 10
});

map.addControl(new mapboxgl.NavigationControl());
