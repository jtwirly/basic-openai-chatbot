import streamlit as st
from openai import OpenAI

# Access the secret API key from the 'default' section in st.secrets
api_key = st.secrets["default"]["OPENAI_API_KEY"]

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

user = input("What do you want to ask me?")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": user
        }
    ]
)

print(completion.choices[0].message.content)