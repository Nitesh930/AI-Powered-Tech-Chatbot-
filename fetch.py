import requests
import json

# Replace 'YOUR_API_KEY' with your actual News API key
API_KEY = '5b2e707d847142b6bc6099fcc3ccd961'

# URL with tech-focused domains
url = f'https://newsapi.org/v2/everything?domains=techcrunch.com,wired.com,theverge.com&sortBy=publishedAt&apiKey={API_KEY}'

def fetch_tech_news():
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        
        # Prepare the articles for saving
        articles_data = []
        for article in articles:
            articles_data.append({
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'content': article.get('content', '')  # Include content if available
            })
        
        # Save articles to a JSON file
        with open('tech_news.json', 'w') as f:
            json.dump(articles_data, f, indent=4)
        
        print(f"Saved {len(articles_data)} articles to tech_news.json")
    else:
        print("Failed to fetch news:", response.json().get("message", "Unknown error"))

# Fetch and save the latest technology news articles
fetch_tech_news()
