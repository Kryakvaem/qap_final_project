import pytest

from pages.reg_page import RegPage
from settings import Info

# тест кейсы NNN-001, NNN-002, NNN-003
@pytest.mark.parametrize("url_product", [Info.URL_ELK, Info.URL_START, Info.URL_Key],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("name", ["К", "Далеко-далеко за словесными горами в стр"], ids=["1 symbols", "40 symbols"])
def test_field_name_negative(web_browser, url_product, name):
    """Проверка поле ИМЯ некорректными данными"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert page.tooltip_first_name_field.is_presented(), "Предупреждение не найдено"


# тест кейсы NNN-007, NNN-008, NNN-009
@pytest.mark.parametrize("url_product", [Info.URL_ELK, Info.URL_START, Info.URL_Key],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("name", ["L", "Lo", "Loli", "Lorem ipsum dolor sit amet, c", "Lorem ipsum dolor sit amet, cu",
                                  "Lorem ipsum dolor sit amet, consectetuer"],
                         ids=['1 eng', "2 eng", "4 eng", "29 eng", "30 eng", "40 eng"])
def test_field_name_latin_negative(web_browser, url_product, name):
    """4 Checking the "Name" field with invalid data in Latin"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert page.tooltip_first_name_field.is_presented(), "Предупреждение не найдено"


# тест кейсы NNN-10, NNN-011, NNN-012
@pytest.mark.parametrize("url_product", [Info.URL_ELK, Info.URL_START, Info.URL_Key],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("surname", ["К", "Далеко-далеко за словесными горами в стр"], ids=["1 symbols", "40 symbols"])
def test_field_surname_negative(web_browser, url_product, surname):
    """5 Checking the field "Last name" with invalid Cyrillic data"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(surname)

    page.first_name_field.click()

    assert page.tooltip_first_name_field.is_presented(), "Предупреждение не найдено"


# тест кейсы NNN-13, NNN-014, NNN-015
@pytest.mark.parametrize("url_product", [Info.URL_ELK, Info.URL_START, Info.URL_Key],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("surname", ["Ка", "Яна", "Душа моя озарена неземной рад", "Душа моя озарена неземной радо"],
                         ids=["2 symbols", "3 symbols", "29 symbols", "30 symbols"])
def test_field_surname_positive(web_browser, url_product, surname):
    """6 Сhecking the field "Last name" with valid data in Cyrillic"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(surname)

    page.first_name_field.click()

    assert not page.tooltip_first_name_field.is_presented(), "A tooltip appeared"

# тест кейсы NNN-016, NNN-017, NNN-018
@pytest.mark.parametrize("url_product", [Info.URL_ELK, Info.URL_START, Info.URL_Key],
                         ids=["URL_ЕLK_Web", "URL_START_Web", "URL_Key_Web"])
def test_reg_form(web_browser, url_product):
    """проверка контента на сайте регистраци трех продуктов"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    assert page.name_page_reg.is_presented(), "Элемента нет на странице"
    assert page.first_name_field.is_presented(), "Элемента нет на странице"
    assert page.surname_field.is_presented(), "Элемента нет на странице"
    assert page.email_phone.is_presented(), "Элемента нет на странице"
    assert page.pass_for_reg.is_presented(), "Элемента нет на странице"
    assert page.pass_for_reg_confirm.is_presented(), "Элемента нет на странице"
    assert page.agreement_reg.is_presented(), "Элемента нет на странице"
    assert page.button_continue_on_reg_page.get_text() == Info.reg_text, "Элемента нет на странице"
    assert page.tagline_reg.is_presented(), "Элемента нет на странице"


# тест кейсы NNN-004, NNN-005, NNN-006
@pytest.mark.parametrize("url_product", [Info.URL_ELK, Info.URL_START, Info.URL_Key],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("name", ["Ка", "Яна", "Душа моя озарена неземной рад", "Душа моя озарена неземной радо"],
                         ids=["2 symbols", "3 symbols", "29 symbols", "30 symbols"])
def test_field_name_positive(web_browser, url_product, name):
    """Проверка поле ИМЯ корректными данными"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert not page.tooltip_first_name_field.is_presented(), "Предупреждение появилось"


# тест кейсы NNN-19, NNN-020, NNN-021
@pytest.mark.parametrize("url_product", [Info.URL_ELK, Info.URL_START, Info.URL_Key],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("surname",
                         ["L", "Lo", "Loli", "Lorem ipsum dolor sit amet, c", "Lorem ipsum dolor sit amet, cu",
                          "Lorem ipsum dolor sit amet, consectetuer"],
                         ids=['1 eng', "2 eng", "4 eng", "29 eng", "30 eng", "40 eng"])
def test_field_surname_latin_negative(web_browser, url_product, surname):
    """7 Checking the "Last name" field with invalid data in Latin"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(surname)

    page.first_name_field.click()

    assert page.tooltip_first_name_field.is_presented(), "Предупреждение не найдено"

