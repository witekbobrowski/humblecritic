#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski
# class inspired by https://github.com/sefakilic/goodreads


class Book:
    def __init__(self, book_dict):
        self._book_dict = book_dict

    def __repr__(self):
        return self.title

    @property
    def id(self):
        return self._book_dict["id"]

    @property
    def title(self):
        return self._book_dict["title"]

    @property
    def authors(self):
        if type(self._book_dict["authors"]["author"]) == list:
            return [author_dict["name"] for author_dict in self._book_dict["authors"]["author"]]
        else:
            return [self._book_dict["authors"]["author"]["name"]]

    @property
    def average_rating(self):
        return self._book_dict["average_rating"]

    @property
    def ratings_count(self):
        """Number of ratings for the book"""
        return self._book_dict['ratings_count']

    @property
    def link(self):
        return self._book_dict["link"]
