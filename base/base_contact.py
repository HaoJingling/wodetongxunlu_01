from selenium.webdriver.support.wait import WebDriverWait


class BaseContact:
    def __init__(self,driver):
        self.driver=driver

    def find_element1(self,feature,timeout=10,poll=0.5):

        by,value=feature
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(by,value))
    def click_add_button(self,feature):
        self.find_element1(feature).click()
    def input_text(self,feature,contact):
        self.find_element1(feature).send_keys(contact)
    def click_back_button(self,feature):
        self.find_element1(feature).click()
