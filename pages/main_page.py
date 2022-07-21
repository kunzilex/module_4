from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()

        #link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

        # login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        # login_link.click()

    def should_be_login_link(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


