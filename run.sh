#!/usr/bin/env sh
docker-compose -f postgres.yaml up
FLASK_APP=server.py FLASK_ENV=development flask run --host=0.0.0.0 --port=8000
