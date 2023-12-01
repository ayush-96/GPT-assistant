import os
from openai import OpenAI


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts "
                                  "with creative flair."}
  ]
)

print(completion.choices[0].message)
