#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import unittest
from .context import humblebundle


class TestBundleBuilderSuite(unittest.TestCase):

    @classmethod
    def test_bundle_builder(cls):
        url = "https://www.humblebundle.com/books/code-your-own-games-books"
        bundle = humblebundle.construct_bundle(humblebundle.Builder(url))
        if bundle.title is None or not bundle.tiers:
            raise AssertionError()


if __name__ == '__main__':
    unittest.main()
