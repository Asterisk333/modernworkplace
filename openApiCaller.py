import json

from openai import OpenAI
from os import getenv
from dotenv import load_dotenv


def fetch_news(prompt: str) -> list[dict]:
    load_dotenv()
    client = OpenAI(api_key=getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    raw_text = response.choices[0].message.content.strip()
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        raise ValueError("Antwort war kein valides JSON:\n" + raw_text)
