"""
Motivational quotes API integration
Fetch random quotes from online sources
"""

import requests
import json

class QuotesAPI:
    """Fetch motivational quotes from external APIs"""
    
    @staticmethod
    def get_quote_from_quotable():
        """Get a random quote from quotable.io API"""
        try:
            response = requests.get("https://api.quotable.io/random", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return f"{data['content']} - {data['author']}"
        except Exception as e:
            print(f"Error fetching from Quotable API: {e}")
        return None
    
    @staticmethod
    def get_motivational_quote():
        """Get a motivational quote from zenquotes API"""
        try:
            response = requests.get("https://zenquotes.io/api/random", timeout=5)
            if response.status_code == 200:
                data = response.json()[0]
                return f"{data['q']} - {data['a']}"
        except Exception as e:
            print(f"Error fetching from ZenQuotes API: {e}")
        return None


if __name__ == "__main__":
    quotes_api = QuotesAPI()
    
    print("Testing Quotable API:")
    quote1 = quotes_api.get_quote_from_quotable()
    if quote1:
        print(f"✓ {quote1}")
    
    print("\nTesting ZenQuotes API:")
    quote2 = quotes_api.get_motivational_quote()
    if quote2:
        print(f"✓ {quote2}")
