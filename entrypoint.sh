export FLASK_APP=main.py
#gunicorn main:app -b 0.0.0.0:25000
python -m flask db init
python -m flask run -h 0.0.0.0 -p 25000
