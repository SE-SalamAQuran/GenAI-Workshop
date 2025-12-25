import requests

requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3",
        "prompt": "Hello",
        "stream": False
    }
)

print("LLM warmed up")
