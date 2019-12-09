FROM vietanhs0817/python:3.7

MAINTAINER vietanhs0817 <vietanhs0817@gmail.com>

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=.:$PYTHONPATH

EXPOSE 5000

CMD ["gunicorn", "-c", "etc/gunicorn.conf.py", "-k", "gevent", "main:app"]
