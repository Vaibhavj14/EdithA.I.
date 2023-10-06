import os
import Openai
from config import apikey


Openai.api_key = apikey

response = Openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write an email to your boss"
    },
    {
      "role": "assistant"
    },
    {
      "role": "user"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)