import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
class TestProductPage:
    def test_the_add_to_basket_button(self, browser):
        browser.get(link)
        time.sleep(30)
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")