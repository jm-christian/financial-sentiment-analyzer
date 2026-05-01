import os
import requests
from dotenv import load_dotenv
from transformers import pipeline

# Load the secret API key from our .env file
load_dotenv()

def get_company_news(company_name):
    print(f"Fetching live news for {company_name}...")
    api_key = os.getenv("NEWS_API_KEY")
    
    # Check if the code can actually see the .env file
    if not api_key:
        print("ERROR: Python cannot find your API key.")
        print("Did you name the file exactly '.env' (with the dot) and save it?")
        return []
        
    url = f"https://newsapi.org/v2/everything?qInTitle={company_name}&language=en&sortBy=publishedAt&apiKey={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    # If NewsAPI rejects our request, print their exact error message
    if data.get("status") != "ok":
        print(f"\nNEWS API ERROR: {data.get('message', 'Unknown error')}\n")
        return []
    
    headlines = []
    for article in data.get("articles", [])[:5]:
        title = article.get("title")
        # NewsAPI sometimes returns "[Removed]" for deleted articles, so we skip those
        if title and title != "[Removed]":
            headlines.append(title)
            
    return headlines
def analyze_headlines(headlines):
    print("Loading FinBERT model...")
    sentiment_analyzer = pipeline("text-classification", model="ProsusAI/finbert")
    
    results = []
    print("Analyzing sentiment...\n")
    for headline in headlines:
        # Analyze each headline one by one
        result = sentiment_analyzer(headline)[0] 
        results.append({"headline": headline, "label": result["label"], "score": result["score"]})
        
    return results

if __name__ == "__main__":
    # 1. Pick a company
    target_company = "Nvidia"
    
    # 2. Fetch the live news
    live_headlines = get_company_news(target_company)
    
    # 3. Analyze the news
    if live_headlines:
        analysis_results = analyze_headlines(live_headlines)
        
        # 4. Print the results cleanly
        for item in analysis_results:
            print(f"Headline: {item['headline']}")
            # Round the score to 2 decimal places (e.g., 0.95)
            print(f"Sentiment: {item['label'].upper()} (Confidence: {item['score']:.2f})\n")
    else:
        print("No headlines found or API error.")