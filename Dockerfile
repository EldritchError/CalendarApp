FROM python:3.10.11

ADD ./src ./src
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]