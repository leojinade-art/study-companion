from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def generate_response(system_prompt, user_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ]
    )

    return response.choices[0].message.content