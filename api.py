import requests

class API:
    def __init__(self):
        # Named Entity Recognition (NER) API details
        self.ner_url = "https://namedentityrecognition.p.rapidapi.com/ner"
        self.ner_headers = {
            "x-rapidapi-key": "8813f81427msh110825a259e2b2dp1ac084jsnbea18cba81a8",  
            "x-rapidapi-host": "namedentityrecognition.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        # Sentiment Analysis API details
        self.sentiment_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"
        self.sentiment_headers = {
            "x-rapidapi-key": "8813f81427msh110825a259e2b2dp1ac084jsnbea18cba81a8",
            "x-rapidapi-host": "twinword-sentiment-analysis.p.rapidapi.com"
        }

        # IP Abuse Check API details
        self.abuse_ip_url = "https://abuse-ip-check.p.rapidapi.com/api/v2/check"
        self.abuse_ip_headers = {
            "x-rapidapi-key": "8813f81427msh110825a259e2b2dp1ac084jsnbea18cba81a8",
            "x-rapidapi-host": "abuse-ip-check.p.rapidapi.com"
        }

    def ner(self, text):
        """Perform Named Entity Recognition (NER) on the given text."""
        payload = {"text": text}  # Request payload

        try:
            response = requests.post(self.ner_url, json=payload, headers=self.ner_headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            return response.json()  # Return the extracted entities
        except requests.exceptions.RequestException as e:
            print("NER API Error:", e)
            return {"error": "NER API request failed"}

    def sentiment(self, text):
        """Perform sentiment analysis on the given text."""
        querystring = {"text": text}

        try:
            response = requests.get(self.sentiment_url, headers=self.sentiment_headers, params=querystring)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            return response.json()  # Return the sentiment analysis result
        except requests.exceptions.RequestException as e:
            print("Sentiment Analysis API Error:", e)
            return {"error": "Sentiment Analysis API request failed"}

    def abuse(self, ip_address):
        """Check if an IP address is associated with abuse."""
        querystring = {"ipAddress": ip_address}

        try:
            response = requests.get(self.abuse_ip_url, headers=self.abuse_ip_headers, params=querystring)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            return response.json()  # Return the abuse check result
        except requests.exceptions.RequestException as e:
            print("Abuse IP Check API Error:", e)
            return {"error": "Abuse IP Check API request failed"}
