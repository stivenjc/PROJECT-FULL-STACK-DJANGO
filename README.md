python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Docker
Para ejecutar el proyecto usando Docker:
```bash
docker-compose up --build
```
El servidor estará disponible en `http://localhost:8000`.