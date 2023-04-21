from .base_page import BasePage


class MainPage(BasePage):

    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

