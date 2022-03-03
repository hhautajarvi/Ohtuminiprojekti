#!/bin/bash
#alustetaan tietokantaa
python src/initialize_database.py
# käynnistetään Flask-palvelin taustalle
export FLASK_APP=src/app
flask run --port 5111 &

 

# suoritetaan testit
robot src/e2e

status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5111)

exit $status
