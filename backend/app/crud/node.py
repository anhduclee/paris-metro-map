from app.core.database import db
from app.schemas.node import NodeFeature, NodeFeatureCollection

async def read_nodes() -> NodeFeatureCollection:
    nodes = await db.nodes.find({}, {"_id": 0}).to_list()
    return NodeFeatureCollection(features=nodes)

async def read_node(id: int) -> NodeFeature:
    node = await db.nodes.find_one({"properties.id": id}, {"_id": 0})
    if not node:
        return None
    return NodeFeature.model_validate(node)

async def update_node_active_status(id: int, active: bool):
    await db.nodes.update_one({"properties.id": id}, {"$set": {"properties.active": active}})