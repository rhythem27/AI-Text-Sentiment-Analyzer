import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="AI Text Sentiment Analyzer",
    page_icon="🤖",
    layout="centered"
)

# API endpoint
API_URL = "http://localhost:8000/analyze"

# Application Title and Description
st.title("🤖 AI Text Sentiment Analyzer")
st.write("Enter a sentence below, and our DistilBERT AI model will analyze its sentiment!")

# Input text area
user_input = st.text_area("Enter your text here:", height=150, placeholder="E.g., I absolutely love the new features in this app!")

# Analyze button
if st.button("Analyze Sentiment", type="primary"):
    if not user_input.strip():
        st.warning("Please enter some text to analyze.")
    else:
        # Show a spinner while waiting for the response
        with st.spinner("Analyzing sentiment..."):
            try:
                # Make the POST request to the FastAPI backend
                response = requests.post(
                    API_URL, 
                    json={"text": user_input},
                    timeout=10  # Important: add timeout for production apps
                )
                
                # Check if the request was successful
                if response.status_code == 200:
                    result = response.json()
                    label = result.get("label")
                    confidence = result.get("confidence", 0.0)
                    
                    # Display the results visually
                    st.subheader("Analysis Results:")
                    
                    # Display label with success/error metrics
                    if label == "Positive":
                        st.success(f"**Sentiment:** {label} 😃")
                    elif label == "Negative":
                        st.error(f"**Sentiment:** {label} 😔")
                    else:
                        st.info(f"**Sentiment:** {label}")
                        
                    # Display confidence scor with a progress bar
                    st.write(f"**Confidence Score:** {confidence:.2%}")
                    st.progress(confidence)
                    
                else:
                    # Handle API errors
                    error_msg = response.json().get("detail", "Unknown error occurred")
                    st.error(f"Error from API: {error_msg}")
                    
            except requests.exceptions.ConnectionError:
                st.error("Failed to connect to the backend. Is the FastAPI server running on http://localhost:8000?")
            except requests.exceptions.Timeout:
                st.error("Request timed out. The backend took too long to respond.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")