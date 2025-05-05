import duckdb

import json
from shapely import wkb

import geopandas as gpd
from shapely import wkb

def list_duckdb_tables():
    con = duckdb.connect('/home/ursha/Documents/GIS/h3', read_only=True)
    query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'main'
        AND table_type = 'BASE TABLE'
    """
    df = con.execute(query).fetchdf()
    con.close()
    return df['table_name'].tolist()




def query_duckdb_table_as_geojson(table_name: str, limit: int = 100):
    # Basic protection against SQL injection
    if not table_name.replace("_", "").isalnum():
        raise ValueError("Invalid table name.")

    # Connect and load spatial extension
    con = duckdb.connect("/home/ursha/Documents/GIS/h3", read_only=True)
    con.execute("INSTALL spatial;")
    con.execute("LOAD spatial;")

    # Query the table and extract WKB geometry
    query = f"""
    SELECT *, ST_AsWKB(geom) AS geom_wkb
    FROM {table_name}
    LIMIT {limit}
    """
    df = con.execute(query).fetchdf()
    con.close()

    # Convert WKB to geometry
    def safe_load_geom(val):
        try:
            if isinstance(val, (bytearray, list)):
                return wkb.loads(bytes(val))
            elif isinstance(val, (bytes, str, memoryview)):
                return wkb.loads(val)
        except Exception as e:
            print(f"Parse error: {e}")
        return None

    df["geometry"] = df["geom_wkb"].apply(safe_load_geom)
    df = df[df["geometry"].notnull()]

    # Create GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

    # Drop non-serializable columns
    non_serializable_cols = [
        col for col in gdf.columns
        if gdf[col].apply(lambda x: isinstance(x, (bytearray, bytes, list))).any()
    ]
    gdf_clean = gdf.drop(columns=non_serializable_cols)

    return gdf_clean.__geo_interface__  # Return as GeoJSON FeatureCollection
