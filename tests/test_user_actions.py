import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class TestUserActions:
    def test_go_to_personal_cabinet_successful(self, user_driver):
        WebDriverWait(user_driver, 3).until(expected_conditions.element_to_be_clickable(Locators.HEADER_PERSONAL_CABINET))
        user_driver.find_element(*Locators.HEADER_PERSONAL_CABINET).click()
        WebDriverWait(user_driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CLIENT_LOGOUT_BUTTON))
        assert user_driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    @pytest.mark.parametrize("main_page_button", [Locators.HEADER_CONSTRUCTOR, Locators.HEADER_LOGO])
    def test_click_constructor_and_logo_successful(self, user_driver, main_page_button):
        WebDriverWait(user_driver, 3).until(expected_conditions.element_to_be_clickable(main_page_button))
        user_driver.find_element(*main_page_button).click()
        assert user_driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_logout_successful(self, user_driver):
        WebDriverWait(user_driver, 3).until(expected_conditions.element_to_be_clickable(Locators.HEADER_PERSONAL_CABINET))
        user_driver.find_element(*Locators.HEADER_PERSONAL_CABINET).click()
        WebDriverWait(user_driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CLIENT_LOGOUT_BUTTON))
        user_driver.find_element(*Locators.CLIENT_LOGOUT_BUTTON).click()
        WebDriverWait(user_driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_PAGE_EMAIL_INPUT))
        assert user_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # нашел так же решение с запоминанием текущего положения скролла через инъекцию JS, но не стал использовать чтобы не
    # усложнять, по этой же логике сделал несколько ассертов в одном тесте, полагаю разбивать на отдельные тесты избыточно.
    def test_choosing_different_filters(self, user_driver):
        user_driver.find_element(*Locators.HEADER_CONSTRUCTOR).click()
        WebDriverWait(user_driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_FILTER_BY_BUN))
        assert 'tab_tab_type_current__2BEPc ' in user_driver.find_element(*Locators.BUTTON_FILTER_BY_BUN).get_attribute('class')
        user_driver.find_element(*Locators.BUTTON_FILTER_BY_SOUSE).click()
        assert 'tab_tab_type_current__2BEPc ' in user_driver.find_element(*Locators.BUTTON_FILTER_BY_SOUSE).get_attribute('class')
        user_driver.find_element(*Locators.BUTTON_FILTER_BY_FILLINGS).click()
        assert 'tab_tab_type_current__2BEPc ' in user_driver.find_element(*Locators.BUTTON_FILTER_BY_FILLINGS).get_attribute('class')
        user_driver.find_element(*Locators.BUTTON_FILTER_BY_BUN).click()
        assert 'tab_tab_type_current__2BEPc ' in user_driver.find_element(*Locators.BUTTON_FILTER_BY_BUN).get_attribute('class')