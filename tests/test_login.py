from data import KNOWN_USER_EMAIL, KNOWN_USER_PASSWORD
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_main_page_login_successful(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BASE_PAGE_LOGIN_BUTTON))
        driver.find_element(*Locators.BASE_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_PAGE_EMAIL_INPUT))
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(KNOWN_USER_EMAIL)
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(KNOWN_USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_CONFIRM_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CLIENT_MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.CLIENT_MAKE_ORDER_BUTTON) is not None

    def test_personal_cabinet_login_successful(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.HEADER_PERSONAL_CABINET).click()
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(KNOWN_USER_EMAIL)
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(KNOWN_USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_CONFIRM_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CLIENT_MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.CLIENT_MAKE_ORDER_BUTTON) is not None

    def test_registration_page_login_successful(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_LOGIN_BUTTON))
        driver.find_element(*Locators.REGISTRATION_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_PAGE_EMAIL_INPUT))
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(KNOWN_USER_EMAIL)
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(KNOWN_USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_CONFIRM_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CLIENT_MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.CLIENT_MAKE_ORDER_BUTTON) is not None

    def test_forgot_password_page_login_successful(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.FORGOT_PASSWORD_LOGIN_BUTTON))
        driver.find_element(*Locators.FORGOT_PASSWORD_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(KNOWN_USER_EMAIL)
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(KNOWN_USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_CONFIRM_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CLIENT_MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.CLIENT_MAKE_ORDER_BUTTON) is not None