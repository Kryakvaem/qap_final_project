import pytest

from pages.auth_page import AuthPage
from settings import Info
import time


# 17 RT-55, RT-62, RT-69 , RT-76 , RT-83
@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK, Info.URL_Online, Info.URL_START, Info.URL_SmartHome,
                          Info.URL_Key],
                         ids=["URL_ЕLK", "URL_Online", "URL_START", "URL_SmartHome", "URL_Key"])
def test_auth_form(web_browser, url_product):

    page = AuthPage(web_browser, url_product)

    if url_product == Info.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    assert page.name_page_auth.is_presented()

    assert page.tab_phone.is_presented()
    assert page.tab_mail.is_presented()
    assert page.tab_login.is_presented()

    assert page.field_username.is_presented()
    assert page.field_password.is_presented()

    assert page.show_password.is_presented()
    assert page.checkbox.is_presented()
    assert page.link_forgot_password.is_presented()
    assert page.button_enter_auth.is_presented()
    assert page.button_enter_with_temp_code.is_presented()
    assert page.agreement_auth.is_presented()

    assert page.link_vk.is_presented()
    assert page.link_ok.is_presented()
    assert page.link_mail.is_presented()
    assert page.link_google.is_presented()
    assert page.link_ya.is_presented()

    assert page.tab_mail.get_text() == Info.tab_mail_text
    assert page.tab_login.get_text() == Info.tab_login_text

    if url_product in [Info.URL_ELK, Info.URL_START]:
        assert page.tab_personal_account.is_presented()
        assert page.tab_personal_account.get_text() == Info.tab_personal_account_text

    if url_product == Info.URL_Online:
        assert not page.tab_personal_account.is_presented()
        assert not page.link_reg.is_presented()
    else:
        assert page.link_reg.is_presented()

    if url_product in [Info.URL_SmartHome, Info.URL_Key]:
        assert not page.tab_personal_account.is_presented()

    assert page.tab_phone.get_text() == Info.tab_phone_text


