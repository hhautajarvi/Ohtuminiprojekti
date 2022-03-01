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
    Create Tip  test  test  test
    Go To Home Page
    Home Page Should Be Open
    Page Should Contain  test  

***Keywords***
Create Tip And Go To Home Page
    Go To Home Page
    Home Page Should Be Open