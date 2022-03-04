#!/bin/bash
#alustetaan tietokantaa
python src/initialize_database.py
# käynnistetään Flask-palvelin taustalle
export FLASK_APP=src/app
flask run --port 5000 &
 

# suoritetaan testit
robot src/tests

status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5000)

exit $status
