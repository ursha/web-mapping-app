from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from shapely.geometry import shape, Polygon
import h3
import geojson

router = APIRouter()

class H3Request(BaseModel):
    geometry: dict   # GeoJSON polygon
    resolution: int  # H3 resolution (0–15)

@router.post("/h3-cells")
def generate_h3_cells(req: H3Request):
    try:
        geom = shape(req.geometry)
        if not isinstance(geom, Polygon):
            raise ValueError("Only Polygon geometries are supported")

        # Generate H3 hexagons intersecting the polygon
        hexes = list(h3.polyfill_geojson(req.geometry, req.resolution))


        # Convert each hex to GeoJSON polygon
        features = []
        for h in hexes:
            boundary = h3.h3_to_geo_boundary(h, geo_json=True)
            poly = geojson.Polygon([boundary + [boundary[0]]])  # close ring
            features.append(geojson.Feature(geometry=poly, properties={"h3": h}))

        return geojson.FeatureCollection(features)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
