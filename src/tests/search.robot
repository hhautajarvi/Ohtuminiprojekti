***Settings***
Resource  resource.robot
Resource  login_resource.robot
Resource  new_tip_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User, Login And Create Tip

***Test Cases***

User Can Search For Tips Based on Title
    Set Search  Uutiset
    Submit Search
    Search Should Succeed And Contain Tip  Uutiset

User Can Search For Tips Based on Title When Case Insensitive
    Set Search  uutiset
    Submit Search
    Search Should Succeed And Contain Tip  Uutiset

User Can Search For Tips Based on Title With The Beginning
    Set Search  uuti
    Submit Search
    Search Should Succeed And Contain Tip  Uutiset

User Can Search For Tips Based on Title With Partial Word
    Set Search  tise
    Submit Search
    Search Should Succeed And Contain Tip  Uutiset

Search Doesn't Work With Wrong Word
    Set Search  news
    Submit Search
    Search Should Succeed And Contain Tip  Ei hakutuloksia kyseisellä haulla.

***Keywords***

Create User, Login And Create Tip
    Create User And Login  saara  saara90  saara123
    Create Tip And Go To Home Page  Uutiset  Yle  https://yle.fi/uutiset  uutiset

Set Search
    [Arguments]  ${Search}
    Input Text  search  ${search}

Submit Search
    Click Button  Etsi

Search Should Succeed And Contain Tip
    [Arguments]  ${message}
    Home Page Should Be Open
    Page Should Contain  ${message}

Search Should Fail With Message
    [Arguments]  ${message}
    Home Page Should Be Open
    Page Should Contain  ${message}
