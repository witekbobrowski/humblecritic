from .context import hr

import unittest


class TestBundleBuilderSuite(unittest.TestCase):
    """Test bundle builder."""

    def test_bundle_builder(self):
        url = "https://www.humblebundle.com/books/functional-programming-books"
        bundle = hr.construct_bundle(hr.Builder(url))
        assert bundle.title != None and bundle.url != None and bundle.tiers != None


if __name__ == '__main__':
    unittest.main()
