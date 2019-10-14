import settings

class AllBooksPage():

    def __init__(self, driver):

        self.driver = driver

        self.all_books_link_text = 'All books'
        self.created_book_link_text = settings.BOOK_TITLE

    def click_all_books(self):
        self.driver.find_element_by_link_text(self.all_books_link_text).click()

    def verify_added_book_present_in_all_books(self):
        book_element = self.driver.find_element_by_link_text(settings.BOOK_TITLE)
        assert book_element.text == settings.BOOK_TITLE
