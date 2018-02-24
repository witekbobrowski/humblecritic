#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski


class Tier:

    def __init__(self, title, price, items):
        self.title = title
        self.price = price
        self.items = items

    def __repr__(self):
        output = "{0.title} Tier:".format(self)
        for item in self.items:
            output += "\n - {0}".format(item)
        return output
