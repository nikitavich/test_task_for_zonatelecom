import time

from selenium.webdriver.common.by import By


class TestYandex:
    def test_input_field(self, driver):
        driver.get(
            'https://passport.yandex.ru/auth/add?origin=dzen&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fuuid%3D41c22b8e-1071-4ae0-91c6-de18105b355d%26retpath%3Dhttps%253A%252F%252Fdzen.ru%252F%253Fask_permissions%253D1&backpath=https%3A%2F%2Fdzen.ru%2F-chunked%2F%3Fyredirect%3Dtrue%26utm_referer%3Dwww.google.com')
        assert driver.find_element(By.NAME, 'login').is_displayed(), 'Поле ввода не отображается'

    def test_enter_button(self, driver):
        driver.get(
            'https://passport.yandex.ru/auth/add?origin=dzen&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fuuid%3D41c22b8e-1071-4ae0-91c6-de18105b355d%26retpath%3Dhttps%253A%252F%252Fdzen.ru%252F%253Fask_permissions%253D1&backpath=https%3A%2F%2Fdzen.ru%2F-chunked%2F%3Fyredirect%3Dtrue%26utm_referer%3Dwww.google.com')
        assert driver.find_element(By.ID, 'passp:sign-in').is_displayed(), 'Кнопка "войти" не отображается'

    def test_check_validation(self, driver):
        driver.get(
            'https://passport.yandex.ru/auth/add?origin=dzen&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fuuid%3D41c22b8e-1071-4ae0-91c6-de18105b355d%26retpath%3Dhttps%253A%252F%252Fdzen.ru%252F%253Fask_permissions%253D1&backpath=https%3A%2F%2Fdzen.ru%2F-chunked%2F%3Fyredirect%3Dtrue%26utm_referer%3Dwww.google.com')
        driver.find_element(By.NAME, 'login').send_keys('sdkfjbnslkjbnaserflb')
        driver.find_element(By.ID, 'passp:sign-in').click()
        assert driver.find_element(By.ID,
                                   'field:input-login:hint').is_displayed(), 'Не отображается ошибка "такого аккаунта нет"'

    def test_success_auth(self, driver):
        driver.get(
            'https://passport.yandex.ru/auth/add?origin=dzen&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fuuid%3D41c22b8e-1071-4ae0-91c6-de18105b355d%26retpath%3Dhttps%253A%252F%252Fdzen.ru%252F%253Fask_permissions%253D1&backpath=https%3A%2F%2Fdzen.ru%2F-chunked%2F%3Fyredirect%3Dtrue%26utm_referer%3Dwww.google.com')
        driver.find_element(By.NAME, 'login').send_keys('testforzonatelecom')
        driver.find_element(By.ID, 'passp:sign-in').click()
        driver.find_element(By.NAME, 'passwd').send_keys('zonatelecom')
        driver.find_element(By.ID, 'passp:sign-in').click()
        time.sleep(3)
        assert driver.current_url == 'https://dzen.ru/?ask_permissions=1', 'Авторизация не прошла'

    def test_check_password_error(self, driver):
        driver.get(
            'https://passport.yandex.ru/auth/add?origin=dzen&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fuuid%3D41c22b8e-1071-4ae0-91c6-de18105b355d%26retpath%3Dhttps%253A%252F%252Fdzen.ru%252F%253Fask_permissions%253D1&backpath=https%3A%2F%2Fdzen.ru%2F-chunked%2F%3Fyredirect%3Dtrue%26utm_referer%3Dwww.google.com')
        driver.find_element(By.NAME, 'login').send_keys('testforzonatelecom')
        driver.find_element(By.ID, 'passp:sign-in').click()
        driver.find_element(By.NAME, 'passwd').send_keys('wrongpassword')
        driver.find_element(By.ID, 'passp:sign-in').click()
        assert driver.find_element(By.ID, 'field:input-passwd:hint'), 'Не отображается сообщение о неверном пароле'
