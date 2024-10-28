import json
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# # Download necessary NLTK data files (run this once if not already downloaded)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Initialize tokenizer, lemmatizer, and stopwords
tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove non-alphanumeric characters (keeping spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Tokenize the text
    tokens = tokenizer.tokenize(text)
    # Remove stopwords and lemmatize
    cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    # Join tokens back into a string
    return ' '.join(cleaned_tokens)

# Load the fetched articles from a JSON file (if you have already saved them)
with open('tech_news.json', 'r') as f:  # Adjust filename if necessary
    articles = json.load(f)

# Preprocess and save cleaned articles
cleaned_articles = []
for article in articles:
    cleaned_article = {
        'title': article['title'],
        'cleaned_title': preprocess_text(article['title']),
        'description': article['description'],
        'cleaned_description': preprocess_text(article['description']) if article['description'] else ''
    }
    cleaned_articles.append(cleaned_article)

# Save the cleaned articles to a new JSON file
with open('tech_news_cleaned.json', 'w') as f:
    json.dump(cleaned_articles, f, indent=4)

print("Cleaned articles saved to tech_news_cleaned.json")
