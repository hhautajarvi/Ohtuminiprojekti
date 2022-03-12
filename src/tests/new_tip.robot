***Settings***
Resource  resource.robot
Resource  new_tip_resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User, Login And Go To New Tip

***Test Cases***
Submit New Tip With Title
    Set Title  NewTip
    Submit Tip 
    Submit Should Succeed And Contain Tip  NewTip

Submit New Tip With Author And Title And Url And Description
    Set Title  something
    Set Author  author_name
    Set URL  https://www.youtube.com/
    Set Description  something
    Submit Tip 
    Submit Should Succeed And Contain Tip  something, author_name, something

Submit New Tip With Too Short Title
    Set Title  so
    Set URL  https://www.youtube.com/
    Set Description  something
    Submit Tip 
    Submit Should Fail With Message  Anna otsikko 3-50 merkin pituisena

Submit New Tip With Too Long Title
    Set Title  sofdasfdasfdsafdsafdsafdsafdsafdsafdsafdsadfdfdsafdgfdshgfdhgfdjhgjhgfjhgdjhgfdhgf
    Set URL  https://www.youtube.com/
    Set Description  something
    Submit Tip 
    Submit Should Fail With Message  Anna otsikko 3-50 merkin pituisena

Submit New Tip With ISBN
    Set ISBN   9789511236764
    Submit ISBN Tip
    Submit Should Succeed And Contain Tip  Kalevala

Submit New Tip With ISBN And Description
    Set ISBN   9789511236764
    Set ISBN-description  testikirja
    Submit ISBN Tip
    Submit Should Succeed And Contain Tip  testikirja

Submit New Tip With Non-ISBN Number
    Set ISBN   123
    Set ISBN-description  testikirja
    Submit ISBN Tip
    Submit Should Fail With Message  Numero ei ole kelpaava ISBN-numero

Submit New Tip With Nonexistent ISBN
    Set ISBN   9789510466810
    Set ISBN-description  testikirja
    Submit ISBN Tip
    Submit Should Fail With Message  ISBN-numerolla ei löytynyt kirjaa
