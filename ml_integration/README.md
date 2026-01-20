# ML Integration

This project is a microservice that trains a text classification model to predict task priority (high/low)
based on descriptions and provides a REST API for real-time predictions.

## How to run
1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run _main.py_ file
4. Navigate to Swagger UI:
   ```bash
   http://0.0.0.0:8000/docs
5. Choose _POST /predict_ and press _Try it out_ button