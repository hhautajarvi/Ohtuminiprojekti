***Keywords***
Go To New Tip
    Go To New Tip Page
    New Tip Page Should Be Open

Set Title
    [Arguments]  ${Title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${Author}
    Input Text  author  ${author}

Set URL
    [Arguments]  ${Title}
    Input Text  url  ${title}

Set Description
    [Arguments]  ${Title}
    Input Text  description  ${title}

Set ISBN
    [Arguments]  ${Title}
    Input Text  isbn_number  ${title}

Set ISBN-description
    [Arguments]  ${Title}
    Input Text  isbn_description  ${title}

Submit Tip
    Click Button  Lisää uusi vinkki

Submit ISBN Tip
    Click Button  Lisää ISBN-vinkki

Submit Should Succeed And Contain Tip 
    [Arguments]  ${message}
    Home Page Should Be Open
    Page Should Contain  ${message}

Submit Should Fail With Message
    [Arguments]  ${message}
    New Tip Page Should Be Open
    Page Should Contain  ${message}

Create Tip And Go To Home Page
    [Arguments]  ${Title}  ${Author}  ${Url}  ${Description}
    Go To New Tip Page
    Set Title  ${Title}
    Set Author  ${Author}
    Set URL  ${Url}
    Set Description  ${Description}
    Submit Tip
    Go To Home Page
    Home Page Should Be Open

