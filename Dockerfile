FROM python:3.7

RUN pip install pipenv
ADD Pipfile* ./
RUN set -e && pipenv install --deploy --system --clear

WORKDIR app
COPY . .
RUN chmod +x manage.py

CMD ./manage.py collectstatic && ./manage.py migrate && ./manage.py runserver 0.0.0.0:8000
