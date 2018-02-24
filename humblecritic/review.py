#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import argparse as ap
import humblecritic.goodreads as gr
import humblecritic.humblebundle as hb
import humblecritic.config as config


def review_bundle(bundle):
    if bundle.type is hb.BundleType.books:
        return get_goodreads_reviews_for(bundle)
    else:
        print(
            "[ERROR] Only the books or comics bundles are supported at the moment :(.")
        return None


# Goodreads
def check_goodreads_keys(keys):
    if keys["developer-key"] is not None and keys["secret"] is not None:
        return
    if keys["developer-key"] is None:
        print("[WARNING] developer key for goodreads api is missing!")
        keys["developer-key"] = input(
            "Please enter developer key for goodreads API:")
    if keys["secret"] is None:
        print("[WARNING] secret for goodreads api is missing!")
        keys["secret"] = input("Please enter secret for goodreads API:")
    if input("Do you wish to save them in the rc file at '" + str(config.path_to_rc_file) + "'? [Y/n]") is "Y":
        config.saveGoodreadsKeys(keys)
    return keys


def get_goodreads_reviews_for(bundle):
    keys = config.getGoodreadsKeys()
    check_goodreads_keys(keys)
    client = gr.GoodreadsClient(keys["developer-key"], keys["secret"])
    print("Searching Goodreads for best book match...")
    for tier in bundle.tiers:
        for book in tier.items:
            best_match_index = 0
            resp = client.search_book(book.title)
            if len(resp) == 0:
                print("[Failure] No results for :", book.title)
            else:
                print("[Success]", resp[best_match_index]["title"],
                      "was found in Goodreads database.")
                book.meta_item = client.show_book(resp[best_match_index]["id"]["#text"])
