db.nodes.insertMany(require('/nodes.json'));
db.edges.insertMany(require('/edges.json'));

db.nodes.createIndex({ "geometry": "2dsphere" });
db.nodes.createIndex({ "properties.id": 1 }, { unique: true });
db.nodes.createIndex({ "properties.active": 1, "properties.child.id": 1 });

db.edges.createIndex({ "properties.id": 1 }, { unique: true });
db.edges.createIndex({ "properties.active": 1, "properties.start": 1 });
db.edges.createIndex({ "properties.active": 1, "properties.end": 1 });