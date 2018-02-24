#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from . import scraper
from .bundle import Bundle
from .bundle import BundleType
from .tier import Tier
from .item import Item


def construct_bundle(builder):
    builder.new_bundle()
    builder.build_url()
    builder.build_title()
    builder.build_type()
    builder.build_tiers()
    return builder.bundle


class Builder:

    def __init__(self, url):
        self.bundle = None
        self.url = url
        self.content = scraper.get_page_content(url)

    def new_bundle(self):
        self.bundle = Bundle()

    def build_url(self):
        self.bundle.url = self.url

    def build_type(self):
        self.bundle.type = BundleType(scraper.get_bundle_type(self.url))

    def build_title(self):
        self.bundle.title = scraper.get_bundle_title(self.content)

    def build_tiers(self):
        tiers = []
        scraped_tiers = scraper.get_tiers(self.content)
        for tier in scraped_tiers:
            title = tier["title"]
            price = tier["price"]
            items = [Item(item) for item in tier["items"]]
            tiers.append(Tier(title, price, items))
        self.bundle.tiers = tiers
