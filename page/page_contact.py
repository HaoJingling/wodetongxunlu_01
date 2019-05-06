from selenium.webdriver.common.by import By

from base.base_contact import BaseContact
from page.page_add import AddPage
from page.page_add_button import AddButton
from page.page_get_text import PageGet


class PageContact:
    def __init__(self,driver):
        self.driver=driver

#@property，将方法调用时转换为属性的调用，实际调用不用加（），但是每个函数对应必须加返回值
    @property
    def page_add_button(self):
        return AddButton(self.driver)

    @property
    def add_page(self):
        return AddPage(self.driver)

    @property
    def page_get_save_text(self):
        return PageGet(self.driver)











