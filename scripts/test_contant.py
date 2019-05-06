from time import sleep

import pytest
import time


# server 启动参数
from base import base_driver
from base.base_data import data
from page.page_contact import PageContact
from page.page_get_text import PageGet


class TestContact:
    def setup(self):
        self.driver=base_driver.base_driver()
        self.page=PageContact(self.driver)
    @pytest.mark.parametrize("args",data("data","test_add_phone"))
    # @pytest.mark.parametrize(("name", "nickname", "telephone"),
    #                          [("xz", "xx", "12233344555"), ("xl", "l", "122333555555")])
    def test_add_contact(self,args):
        name=args["name"]
        nickname=args["nickname"]
        telephone=args["phone"]
        self.page.page_add_button.add_button()
        self.page.add_page.add_text_name(name)
        self.page.add_page.add_text_nickname(nickname)
        self.page.add_page.add_text_tel(telephone)
        time.sleep(2)
        self.page.add_page.add_back()
        time.sleep(2)

        assert self.page.page_get_save_text.page_get_text() == name
