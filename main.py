import chromadb
from chromadb.utils import embedding_functions

# Define the embedding function using SentenceTransformers
ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Create a new instance of ChromaClient to interact with the Chroma DB
client = chromadb.Client()

# Define the name for the collection to be created or retrieved
collection_name = "my_grocery_collection"


def main():
    try:
        collection = client.create_collection(
            name=collection_name,
            metadata={"description": "A collection for storing grocery data"},
            configuration={"hnsw": {"space": "cosine"}, "embedding_function": ef},
        )
        print(f"Collection created: {collection.name}")

        texts = [
            "fresh red apples",
            "organic bananas",
            "ripe mangoes",
            "whole wheat bread",
            "farm-fresh eggs",
            "natural yogurt",
            "frozen vegetables",
            "grass-fed beef",
            "free-range chicken",
            "fresh salmon fillet",
            "aromatic coffee beans",
            "pure honey",
            "golden apple",
            "red fruit",
        ]

        ids = [f"food_{index + 1}" for index, _ in enumerate(texts)]

        collection.add(
            documents=texts,
            metadatas=[{"source": "grocery_store", "category": "food"} for _ in texts],
            ids=ids,
        )

        # Retrieve all the items (documents) stored in the collection
        # The `get` method fetches all data from the collection
        all_items = collection.get()
        # Log the retrieved items to the console for inspection
        # This will print out all the documents, IDs, and metadata stored in the collection
        print("Collection contents:")
        print(f"Number of documents: {len(all_items['documents'])}")

        perform_similarity_search(collection)

    except Exception as error:  # Catch any errors and log them to the console
        print(f"Error: {error}")


def perform_similarity_search(collection):
    try:
        # query_term = "apple"
        query_term = ["red", "fresh"]

        if isinstance(query_term, str):
            query_term = [query_term]

        results = collection.query(
            query_texts=query_term,
            n_results=3,  # Retrieve top 3 results
        )
        print(f"Query results for '{query_term}':")
        print(results)

        # Check if no results are returned or if the results array is empty
        if not results or not results["ids"] or len(results["ids"][0]) == 0:
            # Log a message indicating that no similar documents were found for the query term
            print(f'No documents found similar to "{query_term}"')
            return

        print(f'Top 3 similar documents to "{query_term}":')
        # Access the nested arrays in 'results["ids"]' and 'results["distances"]'
        for q in range(len(query_term)):
            print(f'Top 3 similar documents to "{query_term[q]}":')
            # Access the nested arrays in 'results["ids"]' and 'results["distances"]'
            for i in range(min(3, len(results["ids"][q]))):
                doc_id = results["ids"][q][i]  # Get ID from 'ids' array
                score = results["distances"][q][i]  # Get score from 'distances' array
                # Retrieve text data from the results
                text = results["documents"][q][i]
                if not text:
                    print(f' - ID: {doc_id}, Text: "Text not available", Score: {score:.4f}')
                else:
                    print(f' - ID: {doc_id}, Text: "{text}", Score: {score:.4f}')

    except Exception as error:
        print(f"Error in similarity search: {error}")


if __name__ == "__main__":
    main()
