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
python manage.py runserver