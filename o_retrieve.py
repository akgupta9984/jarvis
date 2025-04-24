import requests
from fake_useragent import UserAgent

def search_internet(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        'user-Agent': UserAgent().random,
        'Accept-language': 'en-US,en;q=0.9',
    }
    
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        return response.text  # Return the HTML content or parse it for specific results
    else:
        return "Sorry, I couldn't retrieve the search results."
 