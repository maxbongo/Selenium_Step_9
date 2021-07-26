link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert button > 0, 'Кнопка покупки отсутствует'


#pytest -s -v --browser_name=chrome --language=es  test_items.py
