#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from enum import Enum


class Item:

    def __init__(self, title, item_type):
        self.title = title
        self.type = item_type

    def __repr__(self):
        return self.title


class ItemType(Enum):
    BOOK = 1
