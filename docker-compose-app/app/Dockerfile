FROM python:alpine

WORKDIR /app

# Выполнить определённую команду
RUN pip install pymongo

COPY . .

CMD [ "python", "main.py" ]