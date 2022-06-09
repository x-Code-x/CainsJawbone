from arango import ArangoClient

client = ArangoClient(hosts='http://127.0.0.1:8529')


db = client.db('_system', username='root', password = 'openSesame')

db.collections()
#pages = db.collection("Page")

#pages.name
