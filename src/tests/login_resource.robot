***Keywords***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Login Credentials
    Click Button  Lähetä

Create User And Login
    Create User  Seppo  seppo52  seppo123
    Go To Login Page
    Set Username  seppo52
    Set Password  seppo123
    Submit Login Credentials

Create User, Login And Go To Home Page
    Create User And Login
    Go To Home Page
    Home Page Should Be Open

Create User, Login And Go To New Tip
    Create User And Login
    Go To New Tip

Logout
    Click Link  Kirjaudu ulos