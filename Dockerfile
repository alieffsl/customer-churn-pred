FROM python:3.9-slim

# COPY app.py app.py
WORKDIR /app

RUN apt-get update 

COPY . .

COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install streamlit
RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]