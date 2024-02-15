*** Settings ***
Library           SeleniumLibrary
...                Generate Report
...                Open Browser
...                Close Browser
...                Log Source    console   # Включить логирование в консоль
Resource          constants.robot


*** Test Cases ***
Test About Link
    [Documentation]    Test the About link functionality
    [Tags]             about-link
    Open Browser       ${URL}    chrome
    Maximize Browser Window
    Click Element      //a[.//text()= 'About']
    Wait Until Location Is    ${ABOUT_URL}
    Location Should Be    ${ABOUT_URL}
    Capture Page Screenshot    # Сохранение скриншота страницы
    Close Browser

