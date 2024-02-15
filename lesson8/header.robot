*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser    https://www.epam.com/    Chrome
Suite Teardown    Close All Browsers
...                Generate Report
...                Log Source    console
Resource          constants.robot


*** Test Cases ***
Localization of Header
    # Проверка языка страницы
    ${language} =    Get Element Attribute    xpath=//html    lang
    Should Be Equal As Strings    ${language}    en

    # Получаем ссылки из хедера
    @{actual_header_links}=    Get WebElements    xpath=//nav[@class='header__nav']//a

    # Проверяем соответствие ожидаемых ссылок
    FOR    ${link}    IN    @{actual_header_links}
        ${index}=    Get Index From List    ${actual_header_links}    ${link}
        ${expected_link}=    Get From List    ${EXPECTED_HEADER_LINKS}    ${index}
        ${actual_link_text}=    Get Text    ${link}
        Should Be Equal As Strings    ${actual_link_text}    ${expected_link}
    END
