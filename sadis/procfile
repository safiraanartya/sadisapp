web: gunicorn myapp.wsgi --log-file
web: python sadis/manage.py migrate && gunicorn myapp.wsgi:application --bind 0.0.0.0:$3306