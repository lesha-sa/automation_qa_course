from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    #form fields
    FULL_NAME = (By.CSS_SELECTOR, 'input[placeholder="Full Name"]')
    EMAIL = (By.XPATH, '//*[@placeholder="name@example.com"]')
    CURRENT_ADDRESS = (By.XPATH, '//*[@id = "currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//*[@id = "permanentAddress"]')
    SUBMIT = (By.XPATH, '//*[@id = "submit"]')

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ('.//ancestor::span[@class="rct-text"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


