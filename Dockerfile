FROM ubuntu:22.04

RUN apt update && apt install -y python3.11 python3-pip python3.11-dev python3.11-distutils libpq-dev

RUN pip install pipenv==2022.12.19

WORKDIR /home/appuser

EXPOSE 8000

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy

COPY . .

CMD ["pipenv", "run", "gunicorn", "-c", "/home/appuser/gunicorn.conf.py", "src.api.app:app"]
