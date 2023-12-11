from openai import OpenAI
import os 
os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)