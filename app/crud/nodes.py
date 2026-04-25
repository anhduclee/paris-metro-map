import json

from app.core.database import db

async def create_collection_nodes():
    collections = await db.list_collection_names()
    if "nodes" not in collections:
        await db.create_collection("nodes")
        await db.nodes.create_index({"geometry": "2dsphere"})
        await db.nodes.create_index({"properties.id": 1})

    if await db.nodes.count_documents({}) > 0:
        return
    
    with open("nodes.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        await db.nodes.insert_many(data)

async def drop_collection_nodes():
    collections = await db.list_collection_names()
    if "nodes" in collections:
        await db.drop_collection("nodes")

async def read_node(id: int) -> dict:
    node = await db.nodes.find_one({"properties.id": id}, {"_id": 0})
    return node