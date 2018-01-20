for start:
    
    python3 -m venv venv

    . venv/bin/activate

    pip3 install -r requirements.txt

    python3 manage.py migrate

    python3 manage.py runserver

