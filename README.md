![Alt Text](https://github.com/Nitesh930/AI-Powered-Tech-Chatbot-/blob/main/techchat.PNG)

## Features

- **Natural Language Processing**: Understands and responds to user queries about technology.
- **Fine-tuning**: Uses a fine-tuned version of the GPT-2 model for improved relevance and context awareness.
- **User-friendly Interface**: A simple HTML frontend that allows users to ask questions easily.
- **FastAPI Backend**: Efficient handling of requests and responses.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tech-chatbot.git
   cd tech-chatbot

2. Create and activate a virtual environment (optional but recommended):
   ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the required packages
   ```python
  pip install -r requirements.txt

6. Download the necessary NLTK data files if you haven't already:
      ```python
      import nltk
      nltk.download('punkt')
      nltk.download('stopwords')
      nltk.download('wordnet')
7. Make sure to have your tech news dataset and other required files in the proper directories.

Usage
1. Start the FastAPI server:
      ```python
      uvicorn backend:app --reload



