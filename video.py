import requests

# Replace with your Brave API key
BRAVE_API_KEY = "BSA6Bugadd2FevoXzXCflMQY4jBgjIr"

def fetch_videos(query: str, limit: int):
    url = "https://api.search.brave.com/res/v1/videos/search"
    params = {
        "q": query,
        "safesearch": "strict",
        "count": limit,
        "search_lang": "en",
        "country": "us",
        "spellcheck": 1
    }
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": BRAVE_API_KEY
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json().get('results', [])
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching videos: {e}")
        return None
