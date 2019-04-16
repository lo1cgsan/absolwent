# Absolwent

Aplikacja Django – materiał szkoleniowy do kursu "Aplikacje i seriwsy sieciowe".

Jeżeli chcesz przetestować aplikację lokalnie:

1. git clone https://github.com/lo1cgsan/absolwent.git
2. cd absolowent
3. python3 -m venv venv
4. source venv/bin/activate.sh
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py makemigrations osoby
8. python manage.py makemigrations wiadomosci
9. python manage.py makemigrations ankiety
10. python manage.py migrate
11. python manage.py createsuperuser
12. python manage.py runserver