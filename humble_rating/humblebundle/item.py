#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from enum import Enum


class Item:

    def __init__(self, title, type):
        self.title = title
        self.type = type

    def __repr__(self):
        return title


class ItemType(Enum):
    BOOK = 1
