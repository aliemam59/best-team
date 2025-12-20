# best-team
CSAI 203 project

Smart Pitch

Team Members: 
Khaled Amr – 202400505 
Ahmed Osama – 204200923 
Ali Emam – 202401429 
Zeyad Mossad – 202401628 

a website for football pitch reservations and bookings to ensure you always find the perfect price/time/location to play football

## Run locally (recommended)

1. Copy `.env.sample` to `.env` and edit values.
2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the app:

```bash
export FLASK_APP=Smart_Pitch/app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
# On Windows PowerShell use `$env:FLASK_APP = "Smart_Pitch/app.py"` and `$env:FLASK_ENV = "development"`
```

## Run with Docker

1. Copy `.env.sample` to `.env` and edit values.
2. Build and run with docker-compose:

```bash
docker compose up --build
```

The app will be available at `http://localhost:5000`.
 
