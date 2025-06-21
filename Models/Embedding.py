from langchain.embeddings.base import Embeddings
import requests

class MYEmbedding(Embeddings):
    def __init__(self, endpoint="http://localhost:1234/v1/embeddings"):
        self.endpoint = endpoint

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [self.embed_query(text) for text in texts]

    def embed_query(self, text: str) -> list[float]:
        headers = {"Content-Type": "application/json", "Authorization": "Bearer lm-studio"}
        data = {"model": "Qwen/Qwen3-Embedding-0.6B-GGUF", "input":text}
        response = requests.post(self.endpoint, headers=headers, json=data)
        return response.json()["data"][0]["embedding"]

