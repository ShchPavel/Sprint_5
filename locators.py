from selenium.webdriver.common.by import By


class Locators:
    '''Локаторы для страницы регистрации /register'''
    REGISTRATION_NAME_INPUT = By.CSS_SELECTOR, 'input[type=\'text\']'  # Поле ввода имени
    REGISTRATION_EMAIL_INPUT = By.XPATH, '//*[text()=\'Email\']/../input'  # Поле ввода электронной почты
    REGISTRATION_PASSWORD_INPUT = By.CSS_SELECTOR, 'input[type=\'password\']'  # поле ввода пароля
    REGISTRATION_CONFIRM_BUTTON = By.CSS_SELECTOR, 'button.button_button__33qZ0'  # Кнопка подтверждения регистрации
    REGISTRATION_INCORRECT_PASSWORD_ERROR = By.CSS_SELECTOR, '.input__error'  # Элемент, указывающий на некоррректный пароль
    REGISTRATION_LOGIN_BUTTON = By.CSS_SELECTOR, 'a[href=\'/login\']'  # Кнопка войти

    '''Локаторы для главной страницы'''
    BASE_PAGE_LOGIN_BUTTON = By.XPATH, '//*[text()=\'Войти в аккаунт\']'  # Кнопка войти в аккаунт на главной странице

    '''Локаторы для страницы логина /login'''
    LOGIN_PAGE_EMAIL_INPUT = By.CSS_SELECTOR, '.input__textfield[type=\'text\']'  # Поле ввода почты
    LOGIN_PAGE_PASSWORD_INPUT = By.CSS_SELECTOR, '.input__textfield[type=\'password\']'  # Поле ввода пароля
    LOGIN_CONFIRM_BUTTON = By.CSS_SELECTOR, '.button_button__33qZ0'  # Кнопка войти
    LOGIN_PAGE_TEXT = By.XPATH, '//h2[text()=\'Вход\']'  # Заголовок ВХОД

    '''Локаторы для кнопок, доступных после логина клиента'''
    CLIENT_MAKE_ORDER_BUTTON = By.XPATH, '//*[text()=\'Оформить заказ\']'  # Кнопка оформить заказ
    CLIENT_LOGOUT_BUTTON = By.XPATH, '//button[text()=\'Выход\']'  # Кнопка выхода из профиля /account/profile

    '''Локатор для страницы восстановления пароля /forgot-password '''
    FORGOT_PASSWORD_LOGIN_BUTTON = By.CSS_SELECTOR, 'a[href=\'/login\']'  # Кнопка войти на странице восстановления пароля

    '''Локаторы для шапки\навигации сайта'''
    HEADER_PERSONAL_CABINET = By.CSS_SELECTOR, 'nav>a[href=\'/account\']'  # Кнопка Персональный кабинет в навигации
    HEADER_CONSTRUCTOR = By.XPATH, '//p[text()=\'Конструктор\']/parent::a'  # Кнопка Конструктор в навигации
    HEADER_LOGO = By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2'  # Кнопка на логотипе в навигации

    '''Локаторы для кнопок фильтрации продуктов'''
    BUTTON_FILTER_BY_BUN = By.XPATH, '//span[text()=\'Булки\']/parent::div'  # Кнопка Булки в фильтре
    BUTTON_FILTER_BY_SOUSE = By.XPATH, '//span[text()=\'Соусы\']/parent::div'  # Кнопка Соусы в фильтре
    BUTTON_FILTER_BY_FILLINGS = By.XPATH, '//span[text()=\'Начинки\']/parent::div'  # Кнопка Начинки в фильтре
