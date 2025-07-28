from assistant.task_manager import handle_task
from assistant.calendar_helper import handle_calendar
from assistant.email_helper import handle_email
from assistant.news_weather import get_weather, get_news
from assistant.summarizer import summarize_text
import openai
import config

openai.api_key = config.OPENAI_API_KEY

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def main():
    print("👋 Welcome to your AI Productivity Assistant!")
    print("Type 'help' for available commands.")

    while True:
        cmd = input("\n🧠 Command: ").strip().lower()
        if cmd == "exit":
            print("👋 Goodbye!")
            break
        elif cmd == "task":
            handle_task()
        elif cmd == "calendar":
            handle_calendar()
        elif cmd == "email":
            handle_email()
        elif cmd == "weather":
            print(get_weather("Bangalore"))
        elif cmd == "news":
            print(get_news())
        elif cmd == "summarize":
            text = input("Paste text to summarize:\n")
            print(summarize_text(text))
        elif cmd == "chat":
            prompt = input("Ask me anything: ")
            print(chat_with_gpt(prompt))
        else:
            print("Available: task, calendar, email, weather, news, summarize, chat, exit")

if __name__ == "__main__":
    main()
