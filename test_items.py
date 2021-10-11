import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_has_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    
    try:
        button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    except:
        button = None
        
    assert button is not None, "There is no add to basket button on the page"