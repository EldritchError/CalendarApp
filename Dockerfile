FROM python:3.11.4

ADD ./src ./src
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]