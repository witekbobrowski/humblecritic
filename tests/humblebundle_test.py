#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import unittest
from .context import humblebundle


class TestHumbleBundleScraper(unittest.TestCase):

    bundles = []

    @classmethod
    def test_get_available_bundles(cls):
        cls.bundles = humblebundle.get_available_bundles()
        if not cls.bundles:
            raise AssertionError()

    @classmethod
    def test_bundle_builder(cls):
        for bundle in cls.bundles:
            hb = humblebundle.construct_bundle(humblebundle.Builder(bundle["url"]))
            if hb.title is None or not hb.tiers:
                raise AssertionError()


if __name__ == '__main__':
    unittest.main()
