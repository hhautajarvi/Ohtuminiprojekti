***Settings***
Resource  resource.robot
Resource  login_resource.robot
Resource  new_tip_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User, Login And Create Tip

***Test Cases***

Tip Can Be Deleted
    Click Button  Poista
    Deletion Should Succeed With Message  Poisto onnistui
    Logout

Deleted Tip Is Not Visible
    Click Button  Poista
    Go To Home Page
    Page Should Not Contain  article
    Logout

Tip Cannot Be Deleted If Not Logged In
    Logout
    Page Should Not Contain Button  Poista

Tip Cannot Be Deleted By Another User
    Logout
    Create User And Login  arja  arja52  arja123
    Page Should Not Contain Button  Poista
    Logout

***Keywords***

Deletion Should Succeed With Message
    [Arguments]  ${message}
    Home Page Should Be Open
    Page Should Contain  ${message}

Create User, Login And Create Tip
    Create User And Login  seppo  seppo52  seppo123
    Create Tip And Go To Home Page  article  author_name  https://www.hs.fi/  description