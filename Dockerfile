FROM python:3.9

RUN pip install fastapi uvicorn
RUN pip install pymongo


COPY . /app

WORKDIR /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
