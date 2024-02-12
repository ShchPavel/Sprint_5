from selenium import webdriver
from locators import Locators
from data_generators import KNOWN_USER_EMAIL, KNOWN_USER_PASSWORD
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture()
def user_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*Locators.HEADER_PERSONAL_CABINET).click()
    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_INPUT).send_keys(KNOWN_USER_EMAIL)
    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_INPUT).send_keys(KNOWN_USER_PASSWORD)
    driver.find_element(*Locators.LOGIN_CONFIRM_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.CLIENT_MAKE_ORDER_BUTTON))
    yield driver
    driver.quit()
