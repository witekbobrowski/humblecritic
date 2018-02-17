#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from . import humble_scraper as hs


def construct_bundle(builder):
    builder.new_bundle()
    builder.build_url()
    builder.build_title()
    builder.build_tiers()
    return builder.bundle

# Abstract Builder


class Builder(object):

    def __init__(self, url):
        self.bundle = None
        self.url = url
        self.content = hs.get_page_content(url)

    def new_bundle(self):
        self.bundle = Bundle()

    def build_url(self):
        self.bundle.url = self.url

    def build_title(self):
        self.bundle.title = hs.get_bundle_title(self.content)

    def build_tiers(self):
        tiers = hs.get_tiers(self.content)
        self.bundle.tiers = [
            Tier(tier[0], Price(tier[1][0], tier[1][1])) for tier in tiers]


class Price(object):

    def __init__(self, currency, amount):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return "{0.currency}{0.amount}".format(self)


class Tier(object):

    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __repr__(self):
        output = "{0.price} Tier:".format(self)
        for item in self.items:
            output += "\n - " + item
        return output


class Bundle(object):

    def __init__(self):
        self.url = None
        self.title = None
        self.tiers = None

    def __repr__(self):
        output = "{0.title} \nurl: \'{0.url}\'\n".format(self)
        for tier in self.tiers:
            output += "\n" + str(tier)
        return output
