from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentiment_model import SentimentAnalyzer

# Initialize FastAPI app
app = FastAPI(title="Sentiment Analyzer API")

# Add CORS middleware to allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the SentimentAnalyzer globally
# This ensures the model is loaded only once when the server starts
analyzer = SentimentAnalyzer()

# Define the Pydantic model for the request body
class AnalyzeRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_sentiment(request: AnalyzeRequest):
    """
    Analyze the sentiment of the provided text.
    """
    result = analyzer.analyze_text(request.text)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
        
    return result