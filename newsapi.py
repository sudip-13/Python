import requests
country=input("for which country code news you want ? ")
def get_news(api_key):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,  # Change this to your desired country code
        'apiKey': api_key,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        news_data = response.json()
        return news_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news data: {e}")
        return None

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = 'ec01fa937dd34bbc8f6e574c22c6e5a0'
news_data = get_news(api_key)

if news_data:
      for article in news_data['articles']:
        print(article['title'])
        print(article['description'])
        print(article['url'])
        print('-' * 30)
  