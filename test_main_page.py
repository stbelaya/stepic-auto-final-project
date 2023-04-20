from pages.main_page import go_to_login_page

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)


