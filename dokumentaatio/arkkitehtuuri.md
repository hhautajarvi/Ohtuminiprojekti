# Arkkitehtuurikuvaus
## Rakenne

Services-kansio sisältää sovelluslogiikan, repositories-kansio tietokantatoiminnot ja entities-kansio käyttäjä- ja vinkkiluokat, joita services- ja repositories-kansioiden luokat käyttävät. Templates-kansio sisältää html-sivut.

## Käyttöliittymä

Ohjelmalla on web-käyttöliittymä, joka sisältää kaksi näkymää: etusivu, jossa näkyy lista vinkeistä ja vinkkejä voi poistaa, ja etusivulta on linkki toiselle sivulle, jolla voi lisätä uuden vinkin.

## Sovelluslogiikka 

<img src="https://github.com/hhautajarvi/Ohtuminiprojekti/blob/master/dokumentaatio/kuvat/luokkakaavio.jpg">

VinkkiService vastaa vinkkien lisäämiseen ja muokkaamiseen liittyvistä toiminnoista. Myöhemmin tehdään UserService, joka vastaa käyttäjiin liittyvistä tietokantatoiminnoista. Vastaavasti VinkkiRepository vastaa vinkkeihin liittyvistä tietokantatoiminnoista ja myöhemmin UserRepository käyttäjiin liittyvistä tietokantatoiminnoista. VinkkiService käyttää VinkkiRepositoryn tietoja ja UserService UserRepositoryn tietoja.

## Tietojen tallennus

Tiedot vinkeistä ja käyttäjistä tallennetaan sqlite3-tietokantaan. Apuna käytetään Flaskia. Tietojen tallentamisesta huolehtivat VinkkiRepository- ja UserRepository-luokat.

## Päätoiminnallisuudet

### Vinkin lisääminen

Etusivulta siirrytään linkillä vinkinlisäys-sivulle. Siellä annetaan tietokenttiin pyydetyt tiedot ja painetaan "Lisää vinkki"-painiketta. Painikkeen painamisen jälkeen käyttöliittymä kutsuu VinkkiServicen toimintoa, joka luo vinkin ja kutsuu VinkkiRepositoryn toimintoa, joka lisää tiedon tietokantaan. Käyttäjätiedot lisätään tähän prosessiin myöhemmin.

### Vinkin poistaminen

VinkkiService-luokka kutsuu VinkkiRepositoryn toimintoa, joka muuttaa vinkin näkyvyystiedon tietokantaan.

### Vinkkien katsominen

Luodaan toiminto, joka hakee automaattisesti kaikki näytettävissä olevat vinkin listaksi etusivulle. Käyttöliittymä kutsuu VinkkiServicen toimintoa, joka kutsuu VinkkiRepositoryn toimintoa, joka hakee vinkkien tiedot tietokannasta.

### Rekisteröityminen

Luodaan myöhemmin.

### Sisäänkirjautuminen

Luodaan myöhemmin.
