from data_generators import (generate_random_user_name, generate_random_email,
                             generate_random_six_symbols_password, generate_random_five_symbols_password)
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationPage:
    def test_correct_inputs_login_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(*generate_random_user_name())
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(*generate_random_email())
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(*generate_random_six_symbols_password())
        driver.find_element(*Locators.REGISTRATION_CONFIRM_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_PAGE_TEXT))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_incorrect_password_error_appears(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(*generate_random_user_name())
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(*generate_random_email())
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(*generate_random_five_symbols_password())
        driver.find_element(*Locators.REGISTRATION_CONFIRM_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_INCORRECT_PASSWORD_ERROR))
        assert driver.find_element(*Locators.REGISTRATION_INCORRECT_PASSWORD_ERROR) is not None
