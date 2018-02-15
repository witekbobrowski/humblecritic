from .context import hs

import unittest


class TestSingleSuite(unittest.TestCase):
    """Test single cases."""

    def test_bundle_builder(self):
        url = "https://www.humblebundle.com/books/functional-programming-books"
        bundle = hs.construct_bundle(hs.Builder(url))
        print(bundle)
        assert bundle.title != None and bundle.url != None and bundle.tiers != None


if __name__ == '__main__':
    unittest.main()
