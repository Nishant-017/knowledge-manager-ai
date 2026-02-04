import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SMALL_ENDPOINT = os.getenv("SMALL_MODEL_ENDPOINT")
HEAVY_ENDPOINT = os.getenv("HEAVY_MODEL_ENDPOINT")


class LLMClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def run(self, prompt):
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "messages": [
                {"role": "user", "content": prompt}
            ]
            # "max_completion_tokens":40
        }

        response = requests.post(self.endpoint, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"]


def generate_summary(text):
    prompt = f"Summarize this in 1-2 short lines:\n{text}"
    return small_model.run(prompt)


def generate_tags(text):
    prompt = f"Generate 3-5 short topic tags (comma separated) for this text:\n{text}"
    tags_text = small_model.run(prompt)

    # convert string to list
    tags = [tag.strip() for tag in tags_text.split(",")]
    return tags



small_model = LLMClient(SMALL_ENDPOINT)
heavy_model = LLMClient(HEAVY_ENDPOINT)
