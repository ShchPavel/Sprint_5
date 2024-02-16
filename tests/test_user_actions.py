import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestUserActions:
    def test_go_to_personal_cabinet_successful(self, driver, user_driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.HEADER_PERSONAL_CABINET))
        driver.find_element(*Locators.HEADER_PERSONAL_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CLIENT_LOGOUT_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    @pytest.mark.parametrize("main_page_button", [Locators.HEADER_CONSTRUCTOR, Locators.HEADER_LOGO])
    def test_click_constructor_and_logo_successful(self, driver, user_driver, main_page_button):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(main_page_button))
        driver.find_element(*main_page_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_logout_successful(self, driver, user_driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.HEADER_PERSONAL_CABINET))
        driver.find_element(*Locators.HEADER_PERSONAL_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CLIENT_LOGOUT_BUTTON))
        driver.find_element(*Locators.CLIENT_LOGOUT_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_PAGE_EMAIL_INPUT))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

