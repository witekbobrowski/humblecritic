#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from enum import Enum


class BundleType(Enum):
    books = "books"
    games = "games"
    software = "software"
    mobile = "mobile"


class Bundle:

    def __init__(self):
        self.url = None
        self.title = None
        self.tiers = []
        self.type = None

    def __repr__(self):
        output = "{0.title} \nurl: \'{0.url}\'\n".format(self)
        for tier in self.tiers:
            output += "\n" + str(tier)
        return output
