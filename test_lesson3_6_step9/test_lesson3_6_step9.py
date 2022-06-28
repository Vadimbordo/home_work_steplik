from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_available_product(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    check_available = WebDriverWait(browser, 10)\
        .until(expected_conditions
               .element_to_be_clickable((By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')))
    assert check_available, f"product is not available, status product is {check_available.text}"
