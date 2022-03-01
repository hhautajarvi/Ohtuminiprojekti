***Settings***
Library  SeleniumLibrary
Library  ../AppLibrary.py

***Variables***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${NEW TIP URL}  http://${SERVER}/add_tip

***Keywords***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Lukuvinkkikirjasto

New Tip Page Should Be Open
    Title Should Be  Lisää uusi lukuvinkki

Go To Home Page
    Go To  ${HOME URL}

Go To New Tip Page
    Go To  ${NEW TIP URL}
