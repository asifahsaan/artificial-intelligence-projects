# Gemini API Integration - README

## Overview

This backend API provides harmful image detection using a CNN model, with optional AI-powered image captioning via Google's Gemini API.

## Features

- **CNN-based Image Classification**: Detects harmful/violent content in images
- **AI Image Captioning**: Generates titles and descriptions for non-harmful images using Gemini
- **Two API Endpoints**:
  - `/predict`: CNN classification only
  - `/predict-with-caption`: CNN classification + Gemini captioning for safe images

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Gemini API Key

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

Set the environment variable:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

Or create a `.env` file (see `.env.example`)

### 3. Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### GET `/`

Health check endpoint.

**Response:**
```json
{
  "message": "Harmful Image Detection API is running!"
}
```

### POST `/predict`

Classify image as harmful or non-harmful (CNN only).

**Request:**
- File upload (multipart/form-data)
- Supported formats: JPEG, PNG

**Response:**
```json
{
  "label": "NON_HARMFUL",
  "confidence": 0.1234,
  "threshold": 0.5
}
```

### POST `/predict-with-caption`

Classify image and generate caption if non-harmful.

**Request:**
- File upload (multipart/form-data)
- Supported formats: JPEG, PNG

**Response for non-harmful images:**
```json
{
  "label": "NON_HARMFUL",
  "confidence": 0.1234,
  "threshold": 0.5,
  "caption": {
    "title": "Sunset Over Mountain Range",
    "description": "A vibrant sunset casts warm colors across a mountain landscape. The scene captures the peaceful transition from day to night."
  }
}
```

**Response for harmful images:**
```json
{
  "label": "HARMFUL",
  "confidence": 0.8765,
  "threshold": 0.5
}
```

## Project Structure

```
backend/
├── main.py                      # FastAPI application & endpoints
├── services/
│   ├── __init__.py
│   └── gemini_service.py        # Gemini API integration
├── models/
│   └── best_harmful_detector.keras  # CNN model (auto-downloaded)
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variable template
└── README.md                    # This file
```

## How It Works

1. **Image Upload**: User uploads an image via API
2. **CNN Classification**: Image is classified as HARMFUL or NON_HARMFUL
3. **Conditional Captioning**: 
   - If HARMFUL: Return classification only
   - If NON_HARMFUL: Call Gemini API to generate title + description
4. **Response**: Return combined results to user

## Important Notes

- **Safety Detection**: The CNN model handles all harmful content detection. Gemini is ONLY used for captioning safe images.
- **API Key Required**: The `/predict-with-caption` endpoint requires `GEMINI_API_KEY` to be set.
- **Backward Compatibility**: The original `/predict` endpoint works without Gemini configuration.

## Testing

### Test with cURL

```bash
# Test CNN classification only
curl -X POST "http://localhost:8000/predict" \
  -F "file=@your_image.jpg"

# Test with captioning
curl -X POST "http://localhost:8000/predict-with-caption" \
  -F "file=@your_image.jpg"
```

### Interactive API Documentation

Visit `http://localhost:8000/docs` for Swagger UI documentation.
