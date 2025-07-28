import requests
import config

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.WEATHER_API_KEY}&units=metric"
    data = requests.get(url).json()
    if data.get("main"):
        return f"{city}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
    return "Weather not available"

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={config.NEWS_API_KEY}"
    data = requests.get(url).json()
    headlines = [a['title'] for a in data['articles'][:5]]
    return "\n".join([f"📰 {h}" for h in headlines])
