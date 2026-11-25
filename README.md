# Calma WorkSpace

## Stack
Django + Bootstrap + SQLite + pytest

## Setup & Run

```powershell
git clone https://github.com/<user>/calma-workspace.git
cd calma-workspace
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
<<<<<<< HEAD
python manage.py runserver
=======
python manage.py runserver
>>>>>>> 503e292cf7998742594c40a4f5fc1bf9290b867d
