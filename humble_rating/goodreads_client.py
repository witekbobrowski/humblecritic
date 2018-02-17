#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import requests
import xmltodict


class GoodreadsClient():

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.session = requests.Session()

    def request(self, method, api, params):
        base_url = "http://www.goodreads.com"
        return xmltodict.parse(self.session.request(method, base_url + api, params=params).content)["GoodreadsResponse"]

    def search_book(self, book):
        method = "GET"
        api_path = "/search/index.xml"
        params = {"q": book, "key": self.key}
        return self.request(method, api_path, params)

    def show_book(self, id, format):
        method = "GET"
        api_path = "/book/show." + str(format)
        params = {"format": format, "id": id, "key": self.key}
        return self.request(method, api_path, params)
