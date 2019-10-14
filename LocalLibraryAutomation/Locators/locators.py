import settings

class Locators():

    # Left menu navigators
    create_new_book_link_text = 'Create new book'
    all_books_link_text = 'All books'

    # Add new book page locators
    book_title_id = 'title'
    book_author_id = 'author'
    book_summary_id = 'summary'
    book_isbn_id = 'isbn'
    book_genre_xpath = "//*[starts-with(@type, 'checkbox')]"
    submit_button_xpath = "//*[starts-with(@type, 'submit')]"


    # All books page locators
    created_book_link_text = settings.BOOK_TITLE