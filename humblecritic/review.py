#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import argparse as ap
import humblecritic.goodreads as gr
import humblecritic.humblebundle as hb
import humblecritic.config as config


def review_bundle(bundle):
    if bundle.type is hb.BundleType.BOOK:
        return get_goodreads_reviews_for(bundle)
    else:
        print("[ERROR] Only the books or comics bundles are supported at the moment :(.")
        return None

def check_goodreads_keys(keys):
    if keys["developer-key"] is not None and keys["secret"] is not None:
        return
    if keys["developer-key"] is None:
        print("[WARNING] developer key for goodreads api is missing!")
        keys["developer-key"] = input("Please enter developer key for goodreads API:")
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
    results = []
    for tier in bundle.tiers:
        books = {}
        for book_title in tier.items:
            best_match_index = 0
            resp = client.search_book(book_title)
            if len(resp) == 0:
                print("[Failure] No results for :", book_title)
            else:
                print("[Success]", resp[best_match_index]["title"],
                      "was found in Goodreads database.")
                books[book_title] = client.show_book(
                    resp[best_match_index]["id"]["#text"])
        results.append({"tier": tier, "books": books})
    return results


def book_description(book):
    description = book.title + " by "
    for author in book.authors:
        description += str(author) + ", "
    description += "\n   Average rating of " + str(book.average_rating)
    description += " from " + str(book.ratings_count) + " reviews."
    description += "\n   URL: " + str(book.link) + "\n"
    return description


def output(bundle, results):
    print("\n", bundle.title)
    ratings = []
    for result in results:
        print("\n###", result["tier"].price, "Tier ###\n")
        tier_ratings = []
        for item in result["tier"].items:
            output = " - "
            if item in result["books"]:
                book = result["books"][item]
                tier_ratings.append(float(book.average_rating))
                output += book_description(book)
            else:
                tier_ratings.append(0.0)
                output += str(item) + "was not found..."
            print(output)
        average = float(sum(tier_ratings)) / max(len(tier_ratings), 1)
        ratings += tier_ratings
        print(" # Average rating in this tier:", average)
    average = float(sum(ratings)) / max(len(ratings), 1)
    print(" # Average rating in bundle:", average)
