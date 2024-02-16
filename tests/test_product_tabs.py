from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestProductTabs:
    def test_starter_choice_bun(self, driver, user_driver):
        driver.find_element(*Locators.HEADER_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_FILTER_BY_BUN))
        assert 'tab_tab_type_current__2BEPc ' in driver.find_element(*Locators.BUTTON_FILTER_BY_BUN).get_attribute('class')

    def test_choose_souse(self, driver, user_driver):
        driver.find_element(*Locators.HEADER_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_FILTER_BY_SOUSE))
        driver.find_element(*Locators.BUTTON_FILTER_BY_SOUSE).click()
        assert 'tab_tab_type_current__2BEPc ' in driver.find_element(*Locators.BUTTON_FILTER_BY_SOUSE).get_attribute('class')

    def test_choose_fillings(self, driver, user_driver):
        driver.find_element(*Locators.HEADER_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_FILTER_BY_FILLINGS))
        driver.find_element(*Locators.BUTTON_FILTER_BY_FILLINGS).click()
        assert 'tab_tab_type_current__2BEPc ' in driver.find_element(*Locators.BUTTON_FILTER_BY_FILLINGS).get_attribute('class')

    def test_choose_bun_after_souse(self, driver, user_driver):
        driver.find_element(*Locators.HEADER_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_FILTER_BY_SOUSE))
        driver.find_element(*Locators.BUTTON_FILTER_BY_SOUSE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_FILTER_BY_BUN))
        driver.find_element(*Locators.BUTTON_FILTER_BY_BUN).click()
        assert 'tab_tab_type_current__2BEPc ' in driver.find_element(*Locators.BUTTON_FILTER_BY_BUN).get_attribute('class')

    def test_choose_bun_after_fillings(self, driver, user_driver):
        driver.find_element(*Locators.HEADER_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_FILTER_BY_FILLINGS))
        driver.find_element(*Locators.BUTTON_FILTER_BY_FILLINGS).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_FILTER_BY_BUN))
        driver.find_element(*Locators.BUTTON_FILTER_BY_BUN).click()
        assert 'tab_tab_type_current__2BEPc ' in driver.find_element(*Locators.BUTTON_FILTER_BY_BUN).get_attribute('class')

