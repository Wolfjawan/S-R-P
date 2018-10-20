FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirments.txt
CMD FLASK_APP=server.py FLASK_ENV=development flask run --host=0.0.0.0 --port=8000