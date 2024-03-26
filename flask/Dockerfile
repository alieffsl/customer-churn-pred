FROM python:3.9-slim

WORKDIR /app

RUN apt-get update 

COPY . .

RUN pip install -U pip
RUN pip install Flask
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]