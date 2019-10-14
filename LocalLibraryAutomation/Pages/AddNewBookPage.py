from selenium.webdriver.support.ui import Select
from Locators.locators import Locators
import random
import settings


class AddNewBookPage():

    def __init__(self, driver):
        self.driver = driver

        self.book_title_id      = Locators.book_title_id
        self.book_author_id     = Locators.book_author_id
        self.book_summary_id    = Locators.book_summary_id
        self.book_isbn_id       = Locators.book_isbn_id
        self.book_genre_xpath   = Locators.book_genre_xpath
        self.submit_button_xpath= Locators.submit_button_xpath

    def enter_book_title(self):
        self.driver.find_element_by_id(self.book_title_id).clear()
        self.driver.find_element_by_id(self.book_title_id).send_keys(settings.BOOK_TITLE)

    def select_book_author(self):
        author = Select(self.driver.find_element_by_id(self.book_author_id))
        author.select_by_index(random.randint(0, len(author.options) - 1))

    def enter_book_summary(self):
        self.driver.find_element_by_id(self.book_summary_id).clear()
        self.driver.find_element_by_id(self.book_summary_id).send_keys(settings.BOOK_SUMMARY)

    def enter_book_isbn_id(self):
        isbn_generator = 'ISBN'+str(random.randint(0, 99))
        self.driver.find_element_by_id(self.book_isbn_id).clear()
        self.driver.find_element_by_id(self.book_isbn_id).send_keys(isbn_generator)


    def select_book_genre(self):
        options = self.driver.find_elements_by_xpath(self.book_genre_xpath)
        random.choice(options).click()

    def submit_book_details(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()


