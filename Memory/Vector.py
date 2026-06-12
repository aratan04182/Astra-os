import chromadb

client = chromadb.Client()

collection = client.create_collection(
    "astra_memory"
)

def save(text, id):

    collection.add(
        documents=[text],
        ids=[str(id)]
    )

def search(query):

    return collection.query(
        query_texts=[query],
        n_results=5
    )
