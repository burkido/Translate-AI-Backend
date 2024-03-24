# FastAPI Machine Translation API

This project is a FastAPI-based API for translating text using machine learning models.

You can find the used NLPs here: https://huggingface.co/Helsinki-NLP

## Sample Usage
1. From EN to DE
```json
{
  "source_lang": "en",
  "target_lang": "de",
  "text": "It's too late to talk about what you did."
}

{
    "translated_text": [
        "Es ist zu spät, um darüber zu reden, was du getan hast."
    ]
}
```

2. From TR to ES
```json
{
  "source_lang": "tr",
  "target_lang": "es",
  "text": "Ne yaptığından bahsetmek için çok geç."
}

{
    "translated_text": [
        "Es demasiado tarde para decirte lo que estás haciendo."
    ]
}
```

You can find samples inside the Postman collection located in the root folder. Tests are also included.

## Project Structure

```bash
src/
│
├── api/
│ ├── v1/
│   ├── endpoints/
│   │ └── translate.py
│   └── api.py
│
├── core/
│ ├── config.py
│ └── event_handler.py
│
├── models/
│ └── translate.py
│
├── service/
│ └── model_manager.py
│
├── test/
│ └── translate_test.py
│
├── main.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
````


## Directory Structure

- **api/v1/endpoints/**: Contains endpoint implementations, including text translation.
- **core/**: Core functionalities of the application, such as configuration and event handling.
- **models/**: Code related to api requests and response
- **service/**: Contains service-related code, including model management.
- **test/**: Directory for storing tests, specifically for translation functionality.
- **main.py**: Entry point for the FastAPI application.
- **docker-compose.yml**: Docker Compose configuration for local development.
- **Dockerfile**: Instructions for building a Docker image for deployment.
- **requirements.txt**: Lists Python dependencies required by the application.

## Usage

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

2. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload

3. Acess the API documentation at http://localhost:8000/docs.

For Docker support:

- Build Docker image
    ```bash
    docker build -t fastapi-translation .

- Run Docker container
    ```bash
    docker run -d --name fastapi-container -p 8000:8000 fastapi-translation