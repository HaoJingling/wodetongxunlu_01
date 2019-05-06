from selenium.webdriver.common.by import By

from base.base_contact import BaseContact
get_text_save=By.ID,"com.android.contacts:id/large_title"

class PageGet(BaseContact):
    def page_get_text(self):
        return self.find_element1(get_text_save).text
