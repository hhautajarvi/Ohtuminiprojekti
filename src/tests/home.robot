***Settings***
Resource  resource.robot
Resource  login_resource.robot
Resource  new_tip_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

***Test Cases***

New Tip Link Is Hidden If Not Logged In
    Page Should Not Contain Link  /add_tip

New Tip Link Is Visible If Logged In
    Create User And Login  seppo  seppo52  seppo123
    Page Should Contain Link  /add_tip
    Logout

Click New Tip Link
    Create User And Login  seppo  seppo52  seppo123
    Go To Home Page
    Click Link  /add_tip
    New Tip Page Should Be Open
    Logout

No Previous Tips
    Page Should Contain  Ei vielä lisättyjä lukuvinkkejä

Create Tip And Check If It Is Visible
    Create User And Login  seppo  seppo52  seppo123
    Create Tip And Go To Home Page  test  test  https://hs.fi  test
    Page Should Contain  test
    Logout

Create Tip With Url And Check Url Is Not Visible
    Create User And Login  seppo  seppo52  seppo123
    Create Tip And Go To Home Page  title  author_name  https://www.youtube.com/  description
    Page Should Not Contain   https://www.youtube.com/
    Logout

Create Tip With Url And Check That Page Contains Link
    Create User And Login  seppo  seppo52  seppo123
    Create Tip And Go To Home Page  article  author  https://www.yle.fi/  news
    Page Should Contain Link  https://www.yle.fi/
    Logout
