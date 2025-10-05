Movie Theater Booking App

A Django Based RESTful movie theater booking application

Users Can:
- View Movies
- Book a seat in a given movie
- View booking history
- View already booked seats
- Navigate the UI to get where they want

Setup: 

Create venv:

pip install -r requirements.txt

source myenv/bin/activate

Install requirements:

pip install -r requirements.txt

Run migration code:

python3 manage.py migrate

Add sample data:

python3 manage.py populate_data

Create user:

python3 manage.py createsuperuser

Start Server: 

python3 manage.py runserver 0.0.0.0:3000

Run Tests:

python3 manage.py test

Site Navigation:
/api/movies/
/api/seats/
/api/bookings/

Used:
Django REST framework,
Bootstrap,
Python, 
Gunicorn

Deployed on Render (link): 

AI usage:
Used Claude to help generate movie information, html code and other UI styleization, helped give me python test cases, helped repair errors in code in other python files, code formatting and comments, and documentation understanding and assignment comprehension. 