from Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.create_new_book = Locators.create_new_book_link_text

    def click_create_new_book(self):
        self.driver.find_element_by_link_text(self.create_new_book).click()



