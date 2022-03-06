*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***

Login With Correct Credentials
    Set Username  seppo52
    Set Password  seppo123
    Submit Login Credentials
    Login Should Succeed With Message  Olet kirjautunut sisään

Login With Incorrect Password
    Set Username  seppo52
    Set Password  sepo123
    Submit Login Credentials
    Login Should Fail With Message  Käyttäjätunnus tai salasana eivät täsmää

Login With Nonexistent Username
    Set Username  sepo52
    Set Password  seppo123
    Submit Login Credentials
    Login Should Fail With Message  Käyttäjätunnus tai salasana eivät täsmää

*** Keywords ***

Login Should Succeed With Message
    [Arguments]  ${message}
    Home Page Should Be Open
    Page Should Contain  ${message} 

Create User And Go To Login Page
    Create User  Seppo  seppo52  seppo123
    Go To Login Page
    Login Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
