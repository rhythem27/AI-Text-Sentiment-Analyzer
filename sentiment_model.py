from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        # Initialize the pipeline for sentiment analysis
        # Using default DistilBERT model
        self.analyzer = pipeline("sentiment-analysis")
        
    def analyze_text(self, text: str) -> dict:
        """
        Analyzes the sentiment of the input text.
        
        Args:
            text (str): The text to analyze.
            
        Returns:
            dict: A dictionary containing 'label' ('Positive' or 'Negative') and 'confidence' (float).
        """
        if not text or not text.strip():
            return {"error": "Input text cannot be empty"}
            
        try:
            # The pipeline usually returns [{label: 'POSITIVE', score: 0.99...}]
            result = self.analyzer(text)[0]
            
            # Map default labels to our desired format
            label_mapping = {
                "POSITIVE": "Positive",
                "NEGATIVE": "Negative"
            }
            
            raw_label = result.get('label', '')
            label = label_mapping.get(raw_label.upper(), raw_label)
            confidence = float(result.get('score', 0.0))
            
            return {
                "label": label,
                "confidence": confidence
            }
        except Exception as e:
            return {"error": str(e)}