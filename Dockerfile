FROM python
COPY . /app
RUN pip install --upgrade pip

WORKDIR /app

RUN pip install flask

CMD python app.py






