import json

with open('tech_news_cleaned.json', 'r') as f:
    cleaned_articles = json.load(f)

with open('tech_news.txt', 'w') as f:
    for article in cleaned_articles:
        f.write(article['cleaned_title'] + '\n')  # Writing the cleaned titles as an example
        if article['cleaned_description']:
            f.write(article['cleaned_description'] + '\n')
