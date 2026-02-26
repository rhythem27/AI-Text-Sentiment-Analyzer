# 🤖 AI Text Sentiment Analyzer

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-FF4B4B.svg?logo=streamlit)](https://streamlit.io/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-FFD21E.svg?logo=huggingface)](https://huggingface.co/)
[![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-blueviolet.svg)](https://python-poetry.org/)

An interactive, high-performance web application that leverages natural language processing to identify and measure the sentiment of everyday text. The application uses a finely-tuned local `DistilBERT` model to generate highly accurate contextual interpretations, identifying sentences as either **Positive** or **Negative** along with absolute confidence scoring factors.

---

## 🏗️ Architecture

The project splits the workload cleanly between a specialized backend API and a dynamic interactive dashboard interface:

1. **The Model (`sentiment_model.py`)**: Utilizes the Hugging Face `transformers` library to initialize an offline, standalone Default DistilBERT pipeline. 
2. **The Backend API (`api.py`)**: Powered by FastAPI, this module instantiates our NLP class into memory to save inference load times globally when booting up. It intercepts requests from the front interface securely via CORS mappings and exposes a standardized JSON `/analyze` POST endpoint.
3. **The Frontend (`app.py`)**: Powered by Streamlit, creating a beautiful and entirely Pythonic reactive browser UI. The dashboard sends user queries synchronously to the backend server and translates the backend JSON inferences into visual status labels and responsive progress grids!

---

## 🛠️ Tech Stack

- **Python**: Core Language
- **Poetry**: Project dependency management and isolated virtual execution 
- **FastAPI**: Asynchronous and typed HTTP inference API serving
- **Streamlit**: Rendering frontend visualization elements
- **Hugging Face (`transformers`)**: DistilBERT NLP inference abstractions 
- **PyTorch**: Local tensor execution engine for the Model

---

## 🚀 Getting Started

### Prerequisites

You will need Python 3.11+ installed as well as the [Poetry Dependency Manager](https://python-poetry.org/docs/#installation).

### 1. Installation

Clone this repository to your local machine and install the defined system dependencies using Poetry:

```bash
# Clone the Repository
git clone https://github.com/rhythem27/AI-Text-Sentiment-Analyzer.git
cd AI-Text-Sentiment-Analyzer

# Install Poetry dependencies locally 
poetry install
```

*(Note: Poetry will automatically establish its protected virtual environment context for you!)*

### 2. Running Locally

We provide an executable shell script wrapper `run.sh` to initialize both the FastAPI backend and Streamlit UI process instances sequentially and maintain process locks. 

Launch the platform:

```bash
# Execute the pipeline runner
bash run.sh
```

*(Windows Users executing from a standard Powershell environment should run `.\run.ps1` instead)*.

### 3. Usage

The process runner spins up two services concurrently:
- **FastAPI Backend Swagger Options:** `http://localhost:8000/docs`
- **Streamlit Dashboard Webpage:** `http://localhost:8501`

Navigate to **localhost:8501** from your browser, enter a sentence in the input form, click **Analyze Sentiment**, and the underlying AI will instantly classify its emotive stance! Just press `Ctrl+C` in your execution terminal to terminate both servers.
