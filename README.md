# Financial News Sentiment Analyzer 📈🤖

An end-to-end Python pipeline that automatically fetches live financial news and uses Natural Language Processing (NLP) to analyze market sentiment. 

## 🚀 How It Works
1. **Live Data Fetching:** Uses the `NewsAPI` to dynamically pull the top recent headlines for a target company (e.g., Nvidia, Apple).
2. **AI Sentiment Analysis:** Feeds the headlines into **FinBERT** (a pre-trained NLP model from Hugging Face specifically tuned on financial data).
3. **Classification:** Categorizes each headline as `POSITIVE`, `NEGATIVE`, or `NEUTRAL` alongside a mathematical confidence score.

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Hugging Face `transformers`, PyTorch, FinBERT (`ProsusAI/finbert`)
* **APIs:** NewsAPI
* **Environment:** `python-dotenv` for secure API key management

## 🧠 What I Learned
During this project, I learned how to integrate local neural networks with live external APIs. A key takeaway was learning how to critically evaluate AI output rather than blindly trusting it. 
* *Example:* I discovered that FinBERT sometimes struggles with aggressive market idioms. It initially flagged the phrase *"earnings absolutely crushed expectations"* as highly **Negative** because of the word "crushed," highlighting the importance of context in NLP models!

## 💻 How to Run Locally

1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment and install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file in the root directory and add your NewsAPI key: `NEWS_API_KEY=your_key_here`
5. Run the script: `python src/analyzer.py`