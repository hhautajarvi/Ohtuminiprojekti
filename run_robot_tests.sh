#!/bin/bash
python src/initialize_database.py
# käynnistetään Flask-palvelin taustalle
export FLASK_APP=src/app
flask run --port 5002 &

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]]; 
  do sleep 1; 
done

# suoritetaan testit
robot src/tests

status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5000)

exit $status
