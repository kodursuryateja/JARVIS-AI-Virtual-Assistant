from openai import OpenAI

client = OpenAI(
    api_key = "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",
)

completion = client.chat.completions.create( 
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis, skilled in general tasks like Alexa and Google Cloud."},
    {"role": "user", "content": "What is coding."}
    ]
)
print(completion.choices[0].message)
print(completion.choices[0].message["content"])
