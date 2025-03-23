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
