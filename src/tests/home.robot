***Settings***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

***Test Cases***
Click New Tip Link
    Click Link  /add_tip
    New Tip Page Should Be Open

No Previous Tips
    Page Should Contain  Ei vielä lisättyjä lukuvinkkejä

Create Tip And Check If It Is Visible
    Create Tip  test  test  test  test
    Go To Home Page
    Home Page Should Be Open
    Page Should Contain  test  

Create Tip With Url And Check Url Is Not Visible
    Create Tip  title  author_name  https://www.youtube.com/  description
    Create Tip And Go To Home Page
    Page Should Not Contain   https://www.youtube.com/

Create Tip With Url And Check That Page Contains Link
    Create Tip  article  author  https://www.yle.fi/  news
    Create Tip And Go To Home Page
    Page Should Contain Link  https://www.yle.fi/

***Keywords***
Create Tip And Go To Home Page
    Go To Home Page
    Home Page Should Be Open