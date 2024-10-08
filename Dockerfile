FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV BYTHONUNBUFFERED 1
ENV PYTHONPATH /usr/src/app

COPY . .

RUN pip install 'poetry==1.5.1'
RUN poetry config virtualenvs.create false

RUN poetry install

CMD ["python", "-u", "src/main.py"]
