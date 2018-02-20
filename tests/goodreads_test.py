#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from .context import goodreads
from .context import config
import unittest

class TestGoodreadsClientSuite(unittest.TestCase):

    keys = config.getGoodreadsKeys()
    client = goodreads.GoodreadsClient(keys["developer-key"], keys["secret"])

    def test_show_book(self):
        book_id = 1
        book = self.client.show_book(book_id)
        assert book.title == "Harry Potter and the Half-Blood Prince (Harry Potter, #6)"

    def test_search_books(self):
        book_title = "Advanced Swift"
        books = self.client.search_book(book_title)
        if len(books) == 0:
            assert False
        assert books[0]["title"] == book_title


if __name__ == '__main__':
    unittest.main()
