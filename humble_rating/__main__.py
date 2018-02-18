#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import argparse as ap
import goodreads as gr
import humblebundle as hb

client = gr.GoodreadsClient("dev-key", "secret")


def setup_parser():
    parser = ap.ArgumentParser()
    parser.add_argument('-u', '--url', help="URL [1 or more] to specific HumbleBundle book bundle.",
                        dest='urls', nargs='*', action='store')
    return parser.parse_args()


def get_ratings_for_bundle_at(url):
    print("Scraping HumbleBundle...")
    bundle = hb.construct_bundle(hb.Builder(url))
    print("Searching Goodreads for best book match...")
    search_results = []
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
        search_results.append({"tier": tier, "books": books})
    return (bundle, search_results)


def book_description(book):
    description = book.title + " by "
    for author in book.authors:
        description += str(author) + ", "
    description += "\n   Average rating of " + str(book.average_rating)
    description += " from " + str(book.ratings_count) + " reviews."
    description += "\n   URL: " + str(book.link) + "\n"
    return description


def output(bundle, results):
    print(bundle.title)
    for result in results:
        print("\n", result["tier"].price, "Tier")
        for item in result["tier"].items:
            book = result["books"][item]
            output = " - "
            if item == None:
                output += item + "was not found..."
            else:
                output += book_description(book)
            print(output)


def main():
    args = setup_parser()
    for url in args.urls:
        bundle, results = get_ratings_for_bundle_at(url)
        output(bundle, results)


if __name__ == '__main__':
    main()
