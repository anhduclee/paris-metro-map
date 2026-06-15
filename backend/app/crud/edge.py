from app.core.database import db
from app.schemas.edge import EdgeFeature, EdgeFeatureCollection

async def read_edges() -> EdgeFeatureCollection:
    edges = await db.edges.find({}, {"_id": 0}).to_list()
    return EdgeFeatureCollection(features=edges)

async def read_edge(id: int) -> EdgeFeature:
    edge = await db.edges.find_one({"properties.id": id}, {"_id": 0})
    if not edge:
        return None
    return EdgeFeature.model_validate(edge)

async def update_edge_active_status(id: int, active: bool):
    await db.edges.update_one({"properties.id": id}, {"$set": {"properties.active": active}})