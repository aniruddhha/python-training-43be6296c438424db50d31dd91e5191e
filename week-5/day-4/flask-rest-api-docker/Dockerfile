FROM python:latest

RUN pip3 install pipenv

ENV PROJECT_DIR /restapidemo

WORKDIR ${PROJECT_DIR}

COPY Pipfile .

COPY Pipfile.lock .

COPY . .

RUN pipenv install --deploy 

EXPOSE 5000

CMD ["pipenv", "run", "python", "api.py"]