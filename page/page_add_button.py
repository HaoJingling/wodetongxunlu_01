from selenium.webdriver.common.by import By

from base.base_contact import BaseContact
add_button=By.ID,"com.android.contacts:id/floating_action_button"

class AddButton(BaseContact):

    def add_button(self):
        self.click_add_button(add_button)