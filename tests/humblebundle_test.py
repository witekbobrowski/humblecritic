#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from .context import humblebundle

import unittest


class TestBundleBuilderSuite(unittest.TestCase):

    def test_bundle_builder(self):
        url = "https://www.humblebundle.com/books/functional-programming-books"
        bundle = humblebundle.construct_bundle(humblebundle.Builder(url))
        assert bundle.title != None and bundle.url != None and bundle.tiers != None


if __name__ == '__main__':
    unittest.main()
