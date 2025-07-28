import openai
import config

openai.api_key = config.OPENAI_API_KEY

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Summarize the following text briefly."},
            {"role": "user", "content": text}
        ]
    )
    return response['choices'][0]['message']['content']
