*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Name  Seppo
    Set Username  seppo2
    Set Password  salasana13
    Set Password Confirmation  salasana13
    Submit Register Credentials
    Register Should Succeed

Register With Nonmatching Password And Password Confirmation
    Set Name  Seppo
    Set Username  seppo25
    Set Password  salasana13
    Set Password Confirmation  salasana131
    Submit Register Credentials
    Register Should Fail With Message   Salasana ja salasanan vahvistus eivät täsmää.

Register With No Username
    Set Name  Seppo
    Set Password  salasana13
    Set Password Confirmation  salasana13
    Submit Register Credentials
    Register Should Fail With Message   Kaikkia kenttiä ei ole täytetty.

Register With No Name
    Set Username  seppo2
    Set Password  salasana13
    Set Password Confirmation  salasana13
    Submit Register Credentials
    Register Should Fail With Message   Kaikkia kenttiä ei ole täytetty.

Register With No Password
    Set Name  Seppo
    Set Username  seppo2
    Submit Register Credentials
    Register Should Fail With Message   Kaikkia kenttiä ei ole täytetty.

Register With Username Already Taken
    Set Name  Seppo
    Set Username  seppo12
    Set Password  salasana13
    Set Password Confirmation  salasana13
    Submit Register Credentials
    Home Page Should Be Open
    Click Link  Kirjaudu ulos
    Home Page Should Be Open
    Click Link  Rekisteröidy
    Register Page Should Be Open
    Set Name  UusiSeppo
    Set Username  seppo12
    Set Password  salasana132
    Set Password Confirmation  salasana132
    Submit Register Credentials
    Register Should Fail With Message   Käyttäjätunnus on jo olemassa.

*** Keywords ***

Register Should Succeed
    Home Page Should Be Open

Submit Register Credentials
    Click Button  Rekisteröidy

Set Name
    [Arguments]  ${name}
    Input Text  name  ${name}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}