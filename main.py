from profanity_randomizer import get_profanity
from context_randomizer import get_context
from openai import OpenAI


client = OpenAI()

user_input = input("> ")
prompt = "{} in 1 sentence: {}".format(get_context(), user_input)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": prompt}
  ]
)

response = "{}, {}?!".format(completion.choices[0].message.content.replace('?', ''), get_profanity())
print(response)
