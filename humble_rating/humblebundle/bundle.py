#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski


class Bundle:

    def __init__(self):
        self.url = None
        self.title = None
        self.tiers = None

    def __repr__(self):
        output = "{0.title} \nurl: \'{0.url}\'\n".format(self)
        for tier in self.tiers:
            output += "\n" + str(tier)
        return output
