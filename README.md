# Production-Grade Multimodal Text-to-Image Generation and Analysis System

## Overview

This project implements an end-to-end multimodal machine learning pipeline that generates images from text prompts, analyzes the generated images using a vision-language model, and performs instance segmentation to identify regions of interest. The system is exposed through a RESTful API and is designed with clean, modular, and production-oriented ML engineering practices.

The pipeline integrates three state-of-the-art models:
- **Stable Diffusion** for text-to-image generation
- **CLIP** for semantic image understanding
- **Segment Anything Model (SAM2)** for image segmentation

The application supports both **CPU and GPU environments** and is built to be extensible, testable, and deployment-ready.

---

## Key Features

- Text-to-image generation using Stable Diffusion
- Semantic image analysis using CLIP with confidence scores
- Basic instance segmentation using SAM2
- RESTful API built with FastAPI
- Modular and scalable project structure
- CPU and GPU compatibility
- Input validation, error handling, and logging
- Basic unit and integration testing
- Docker-ready configuration

---

## High-Level Architecture
```
User Request (Text / Image)
↓
REST API
↓
Processing Pipeline
┌──────────────────────────┐
│ Stable Diffusion │ → Image Generation
│ CLIP │ → Concept Analysis
│ SAM2 │ → Segmentation
└──────────────────────────┘
↓
JSON Response
```

---

## Project Structure
```
ext_to_image_pipeline/
│
├── app/
│ ├── main.py # FastAPI application entry point
│ ├── api/
│ │ └── routes.py # API endpoints
│ ├── core/
│ │ ├── config.py # Environment & device configuration
│ │ └── logger.py # Logging utilities
│ ├── models/
│ │ ├── stable_diffusion.py # Text-to-image generation
│ │ ├── clip_model.py # Image analysis with CLIP
│ │ └── sam_model.py # Image segmentation with SAM2
│ ├── pipeline/
│ │ └── processor.py # Orchestrates the ML pipeline
│ ├── schemas/
│ │ └── response.py # API response schemas
│ └── utils/
│ ├── image_utils.py
│ └── encoding.py
│
├── tests/
│ ├── test_generate.py
│ └── test_analyze.py
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .env
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd text_to_image_pipeline
```
### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
## CPU & GPU Configuration

- The system automatically detects available hardware.

- If CUDA is available, the models will run on GPU. Otherwise, the system falls back to CPU

- No manual configuration is required.

## Running the Application
```
uvicorn app.main:app --reload
```

## Once running, access the API documentation at:
```
http://localhost:8000/docs
```

---


## API Endpoints

### 1. Generate Image from Text

**Endpoint**
```

POST /generate

````

**Request**
```json
{
  "prompt": "a futuristic city at sunset"
}
````

**Response**

```json
{
  "request_id": "unique_id",
  "generated_image": "base64_encoded_image",
  "clip_analysis": {
    "concepts": ["city", "buildings", "sunset"],
    "confidence_scores": {
      "city": 0.92,
      "buildings": 0.87,
      "sunset": 0.81
    }
  },
  "basic_segmentation": {
    "masks": [],
    "polygons": []
  }
}
```

---

### 2. Analyze Existing Image

**Endpoint**

```
POST /analyze
```

**Request**

* Image file (`multipart/form-data`)

**Response**

```json
{
  "request_id": "unique_id",
  "clip_analysis": {
    "concepts": [...],
    "confidence_scores": {...}
  },
  "basic_segmentation": {
    "masks": [...],
    "polygons": [...]
  }
}
```

---

## Error Handling & Validation

* Input validation for text and image inputs
* Graceful handling of model loading and inference errors
* Request timeouts for long-running operations
* Structured logging for debugging and monitoring

---

## Testing

Run tests using:

```bash
pytest
```

Includes:

* Unit tests for core pipeline components
* Integration tests for API endpoints
* Error case validation

---

## Docker Support

Build and run the application using Docker:

```bash
docker build -t text-to-image-pipeline .
docker run -p 8000:8000 text-to-image-pipeline
```

---

## Design Decisions

* **FastAPI** chosen for speed, type safety, and automatic API documentation
* **Modular architecture** for maintainability and extensibility
* **Pipeline abstraction** to separate orchestration from model logic
* **Base64 encoding** for easy image transport via REST APIs

---

## Limitations

* SAM2 segmentation is implemented at a basic level due to model complexity
* Advanced region-based analysis and visualization are not enabled by default
* Performance optimization is minimal for clarity and reliability

---

## Future Improvements

* Enhanced region-wise CLIP analysis
* Advanced segmentation visualization overlays
* Model caching and performance optimization
* Asynchronous request handling
* Cloud deployment support

---

## License

This project is intended for evaluation and educational purposes.

```
