*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User, Login And Go To Home Page

*** Test Cases ***

Logout Should Succeed
    Click Link  Kirjaudu ulos
    Logout Should Succeed With Message  Kirjaudu sisään

*** Keywords ***

Logout Should Succeed With Message
    [Arguments]  ${message}
    Home Page Should Be Open
    Page Should Contain  ${message} 

