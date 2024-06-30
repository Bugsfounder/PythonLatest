from openai import OpenAI


# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
def ai(content):
    client = OpenAI(
        api_key="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",
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
            },
            {
                "role": "user",
                "content": content,
            },
        ],
    )

    return completion.choices[0].message


print(ai("Hello"))
