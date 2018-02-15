from bs4 import BeautifulSoup
import requests
import re
import sys

# HumbleBundle HTML Classes
TIER = "main-content-row dd-game-row js-nav-row"
TIER_HEADLINE = "dd-header-headline"
ELEMENT_CAPTION = "dd-image-box-caption-container"
ELEMENT_TITLE = "dd-image-box-caption"

# Functions
def getPageContent(url):
    page = requests.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.content, 'html.parser')


def getBundleTitle(content):
    return content.title.get_text()


def getTierPrice(tier_headline_content):
    string = tier_headline_content.get_text().strip()
    return (re.search('\$(.+?)\ ', string).group(1), "$s")


def getElements(tier_content):
    books = []
    for book_content in tier_content.find_all(class_=ELEMENT_CAPTION):
        books.append(book_content.find(
            class_=ELEMENT_TITLE).get_text().strip())
    return books


def getTiers(content):
    tiers = []
    for tier_content in content.find_all(class_=TIER):
        price = getPrice(tier_content.find(class_=TIER_HEADLINE))
        elements = getElements(tier_content)
        tiers.append((elements, price))
    return tiers
