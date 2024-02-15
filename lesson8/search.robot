*** Settings ***
Library           SeleniumLibrary
Library           String
Resource          constants.robot

*** Test Cases ***
Test Search Python
    [Documentation]    Test the search functionality for the word "Python"
    [Tags]             search-python
    Open Browser       ${URL}    ${BROWSER}
    Maximize Browser Window
    Click Element      ${SEARCH_BUTTON}
    Wait Until Element Is Visible  ${SEARCH_FIELD}
    Input Text         ${SEARCH_FIELD}    Python
    Click Element      ${FIND_BUTTON}
    Wait Until Element Is Visible    ${SEARCH_RESULTS}
    ${results_text}=   Get Text    ${SEARCH_RESULTS}
    ${results_count}=  Get Regexp Matches  ${results_text}  \\d+
    Should Be Equal As Integers    ${results_count}[0]    ${EXPECTED_RESULTS}

*** Keywords ***
Resource          constants.robot
