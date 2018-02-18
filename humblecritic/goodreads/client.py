#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import requests
import xmltodict
from enum import Enum
from .book import Book

class HTTPMethod(Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"

class GoodreadsClient:

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.session = requests.Session()

    def request(self, method, api, params):
        base_url = "http://www.goodreads.com"
        response = self.session.request(method, base_url + api, params=params, timeout=3)
        return xmltodict.parse(response.content)["GoodreadsResponse"]

    def search_book(self, book):
        method = HTTPMethod.GET.value
        api_path = "/search/index.xml"
        params = {"q": book, "key": self.key, "search[field]": "title"}
        response = self.request(method, api_path, params)
        if response["search"]["results"] == None:
            return []
        if type(response["search"]["results"]["work"]) == list:
            return [results["best_book"] for results in response["search"]["results"]["work"]]
        else:
            return [response["search"]["results"]["work"]["best_book"]]

    def show_book(self, id):
        method = HTTPMethod.GET.value
        api_path = "/book/show.xml"
        params = {"format": "xml", "id": id, "key": self.key}
        response = self.request(method, api_path, params)
        return Book(response["book"])
