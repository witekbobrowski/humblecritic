from .context import hr

import unittest


class TestGoodreadsClientSuite(unittest.TestCase):
    """Test GoodreadsClient."""

    def test_show_book(self):
        book_id = 1
        gc = hr.GoodreadsClient("key", "secret")
        results = gc.show_book(book_id, "xml")
        assert results["book"]["title"] == "Harry Potter and the Half-Blood Prince (Harry Potter, #6)"


if __name__ == '__main__':
    unittest.main()
