fetch("http://127.0.0.1:8001/config/mapbox-token")
  .then(res => res.json())
  .then(data => {
    mapboxgl.accessToken = data.token;

    const map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [0, 50.2], // Adjust center if needed
      zoom: 7
    });

    
  })
  .catch(error => console.error("Failed to fetch token:", error));
