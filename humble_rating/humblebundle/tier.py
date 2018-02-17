#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski


class Tier:

    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __repr__(self):
        output = "{0.price} Tier:".format(self)
        for item in self.items:
            output += "\n - {item}".format(self)
        return output
