from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_is_presented(browser):
    browser.get(link)
    basket_form_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(basket_form_button) > 0, "button 'add to basket' not found"
