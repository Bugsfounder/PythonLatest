# Default
import os
from groq import Groq

# Doc : https://console.groq.com/docs/quickstart
client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)


def ai(content):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a friendly virtual assistant named jarvis, skilled in general tasks like alexa, google cloud. Give short responses please.",
            },
            {
                "role": "user",
                "content": content,
            },
        ],
        model="mixtral-8x7b-32768",
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    print(ai("Hello"))
