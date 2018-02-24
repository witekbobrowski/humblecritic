#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os.path
import requests
import re

base_url = "https://www.humblebundle.com/"


def get_page_content(url):
    page = requests.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.content, 'html.parser')


def get_bundle_type(url):
    parsed_url = urlparse(url)
    return os.path.split(parsed_url.path)[0].replace("/", "")


def get_bundle_title(content):
    return content.title.get_text()


def get_tier_price(tier_headline_content):
    string = tier_headline_content.get_text().strip()
    price = re.search('\$(.+?)\ ', string)
    return string if price is None else "$" + price.group(1)


def get_items(tier_content):
    items = []
    item_container_css_class = "dd-image-box-caption-container"
    item_title_css_class = "dd-image-box-caption"
    for item_content in tier_content.find_all(class_=item_container_css_class):
        items.append(item_content.find(
            class_=item_title_css_class).get_text().strip())
    return items


def get_tiers(content):
    tier_css_class = "main-content-row dd-game-row js-nav-row"
    tier_headline_css_class = "dd-header-headline"
    tiers = []
    for tier_content in content.find_all(class_=tier_css_class):
        price = get_tier_price(tier_content.find(
            class_=tier_headline_css_class))
        items = get_items(tier_content)
        tiers.append((items, price))
    return tiers
