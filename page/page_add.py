from selenium.webdriver.common.by import By

from base.base_contact import BaseContact

add_name_text=By.XPATH,"//*[@text='姓名']"
add_nickname_text=By.XPATH,"//*[@text='昵称']"
add_telephone_text=By.XPATH,"//*[@text='电话']"
# add_back_button=By.CLASS_NAME,"android.widget.ImageButton"
add_back_button=By.CLASS_NAME,"android.widget.ImageButton"
class AddPage(BaseContact):
    def add_text_name(self,name):
        self.input_text(add_name_text, name)

    def add_text_nickname(self,nickname):
        self.input_text(add_nickname_text, nickname)

    def add_text_tel(self,telephone):
        self.input_text(add_telephone_text, telephone)

    def add_back(self):
        self.click_back_button(add_back_button)