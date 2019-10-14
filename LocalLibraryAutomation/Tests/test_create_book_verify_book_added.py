from selenium import webdriver
import time
import unittest
import settings
from Pages.HomePage import HomePage
from Pages.AddNewBookPage import AddNewBookPage
from Pages.AllBooksPage import AllBooksPage


class AddBookTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()


    def test_add_book(self):
        driver = self.driver
        self.driver.get(settings.BASE_URL)
        home = HomePage(driver)
        addNewBook = AddNewBookPage(driver)

        home.click_create_new_book()
        time.sleep(1)
        addNewBook.enter_book_title()
        addNewBook.select_book_author()
        addNewBook.enter_book_summary()
        addNewBook.enter_book_isbn_id()
        addNewBook.select_book_genre()
        addNewBook.submit_book_details()
        time.sleep(2)


    def test_verify_added_book_present(self):
        driver = self.driver

        allBooks = AllBooksPage(driver)

        allBooks.click_all_books()
        allBooks.verify_added_book_present_in_all_books()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()







