#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski


class Item:

    def __init__(self, title):
        self.title = title
        self.meta_item = None

    def __repr__(self):
        return self.title
