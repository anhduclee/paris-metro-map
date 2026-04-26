from pydantic import BaseModel

class EdgeGeometry(BaseModel):
    coordinates: list[list[float]]
    type: str = "LineString"

class EdgeGeoPoint2D(BaseModel):
    lon: float
    lat: float

class Station(BaseModel):
    id: int
    name: str
    point: list[float]

class EdgeProperties(BaseModel):
    id: int
    geo_point_2d: EdgeGeoPoint2D
    start: Station
    end: Station
    line: str
    length: float
    color: str
    active: bool

class EdgeFeature(BaseModel):
    type: str = "Feature"
    geometry: EdgeGeometry
    properties: EdgeProperties

class EdgeFeatureCollection(BaseModel):
    type: str = "FeatureCollection"
    features: list[EdgeFeature]