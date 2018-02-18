#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from . import scraper
from .bundle import Bundle
from .tier import Tier
from .item import Item
from .item import ItemType

def construct_bundle(builder):
    builder.new_bundle()
    builder.build_url()
    builder.build_title()
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

    def build_title(self):
        self.bundle.title = scraper.get_bundle_title(self.content)

    def build_tiers(self):
        tiers = []
        scraped_tiers = scraper.get_tiers(self.content)
        for scraped_tier in scraped_tiers:
            price = scraped_tier[1]
            items = [Item(item, ItemType.BOOK) for item in scraped_tier[0]]
            tiers.append(Tier(items, price))
        self.bundle.tiers = tiers
