import json

from app.core.database import db

async def create_collection_edges():
    collections = await db.list_collection_names()
    if "edges" not in collections:
        await db.create_collection("edges")
        await db.edges.create_index({"geometry": "2dsphere"})
        await db.edges.create_index({"properties.start.id": 1})
        await db.edges.create_index({"properties.end.id": 1})
    if await db.edges.count_documents({}) > 0:
        return
    with open("edges.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        await db.edges.insert_many(data)

async def drop_collection_edges():
    collections = await db.list_collection_names()
    if "edges" in collections:
        await db.drop_collection("edges")

