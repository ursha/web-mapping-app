fetch("http://127.0.0.1:8001/config/mapbox-token")
  .then(res => res.json())
  .then(data => {
    mapboxgl.accessToken = data.token;
    const map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [-0.12, 51.5],
      zoom: 10
    });
  })
  .catch(error => console.error("Failed to fetch token:", error));
