FROM python:3.7

ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code

ADD requirements/prod.txt /code/
ADD requirements/common.txt /code/
RUN pip install -r prod.txt
ADD . /code/
EXPOSE 8000
CMD ["gunicorn","-c", "./crawler/gunicorn_conf.py",  "crawler.wsgi:application"]
#CMD ["python", "-m", "http.server",  "8001"]
