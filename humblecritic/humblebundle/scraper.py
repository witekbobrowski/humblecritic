#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import re
import os.path
from urllib.parse import urlparse
from urllib.parse import urljoin
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

base_url = "https://www.humblebundle.com/"


def get_page_content(url):
    page = requests.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.content, 'html.parser')
    return None


def get_available_bundles():
    options = webdriver.firefox.options.Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(base_url)
    content = BeautifulSoup(driver.page_source, 'html.parser')
    bundles_dropdown_css_class = "js-dropdown-button dropdown-button"
    bundle_css_class = "simple-tile-view one-third bundle navbar-tile"
    bundle_title_css_class, bundle_url_css_class = "name", "more-details"
    bundles = []
    dropdown = content.find(class_=bundles_dropdown_css_class)
    for bundle_content in dropdown.find_all(class_=bundle_css_class):
        title = bundle_content.find(class_=bundle_title_css_class).get_text().strip()
        if "MONTHLY" in title:
            continue
        url = bundle_content.find(class_=bundle_url_css_class)["href"].strip()
        url = urljoin(base_url, url)
        type_ = get_bundle_type(url)
        bundles.append({"title": title, "url": url, "type": type_})
    return bundles


def get_bundle_type(url):
    parsed_url = urlparse(url)
    return os.path.split(parsed_url.path)[0].replace("/", "")


def get_bundle_title(content):
    return content.title.get_text()


def get_tier_headline(tier_headline_content):
    return tier_headline_content.get_text().strip()


def get_tier_price(headline):
    price = re.search('\$(.+?)\ ', headline)
    return "$0" if price is None else "$" + price.group(1)


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
        headline = get_tier_headline(
            tier_content.find(class_=tier_headline_css_class))
        price = get_tier_price(headline)
        items = get_items(tier_content)
        tiers.append({"title": headline, "price": price, "items": items})
    return tiers
