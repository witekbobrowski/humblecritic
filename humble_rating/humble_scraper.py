#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import sys

# HumbleBundle HTML Classes
TIER = "main-content-row dd-game-row js-nav-row"
TIER_HEADLINE = "dd-header-headline"
ITEM_CAPTION = "dd-image-box-caption-container"
ITEM_TITLE = "dd-image-box-caption"

# Functions


def get_page_content(url):
    page = requests.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.content, 'html.parser')


def get_bundle_title(content):
    return content.title.get_text()


def get_tier_price(tier_headline_content):
    string = tier_headline_content.get_text().strip()
    return ("$", re.search('\$(.+?)\ ', string).group(1))


def get_items(tier_content):
    items = []
    for item_content in tier_content.find_all(class_=ITEM_CAPTION):
        items.append(item_content.find(class_=ITEM_TITLE).get_text().strip())
    return items


def get_tiers(content):
    tiers = []
    for tier_content in content.find_all(class_=TIER):
        price = get_tier_price(tier_content.find(class_=TIER_HEADLINE))
        items = get_items(tier_content)
        tiers.append((items, price))
    return tiers
