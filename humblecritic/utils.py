#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import json
import argparse
import humblecritic.goodreads as gr


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--link', help="URL [1 or more] to specific HumbleBundle book bundle.",
                        dest='urls', nargs='*', action='store')
    parser.add_argument('-j', '--json', help="Export results to json file.",
                        dest='json_file', action='store')
    return parser.parse_args()


def export_to_json(path, bundles):
    data = []
    for bundle in bundles:
        tiers = []
        for tier in bundle.tiers:
            items = []
            for item in tier.items:
                entry = {}
                if isinstance(item.meta_item, gr.Book):
                    entry = {"id": item.meta_item.id,
                             "title": item.meta_item.title,
                             "authors": item.meta_item.authors,
                             "link": item.meta_item.link,
                             "average_rating": item.meta_item.average_rating,
                             "ratings_count": item.meta_item.ratings_count}
                else:
                    entry = {"id": "",
                             "title": item.title,
                             "authors": "",
                             "link": "",
                             "average_rating": "",
                             "ratings_count": ""}
                items.append(entry)
            tiers.append(
                {"title": tier.title, "price": tier.price, "items": items})
        data.append({"title": bundle.title, "link": bundle.url,
                     "type": bundle.type.value, "tiers": tiers})
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def item_description(item):
    lines = []
    if isinstance(item.meta_item, gr.Book):
        description = item.meta_item.title + " by "
        for author in item.meta_item.authors:
            description += str(author) + ", "
        lines.append(description)
        description = "Average rating of " + \
            str(item.meta_item.average_rating)
        description += " from " + \
            str(item.meta_item.ratings_count) + " reviews."
        lines.append(description)
    else:
        lines = [
            str(item) + "was not found (will not be counted in total score)."]
    return lines


def print_summary(bundle):
    print("\n" + bundle.title)
    ratings = []
    for index, tier in enumerate(bundle.tiers):
        prefix = "│"
        if index is (len(bundle.tiers) - 1):
            print("└── " + tier.title)
            prefix = " "
        else:
            print("├── " + tier.title)
        tier_ratings = []
        for item_index, item in enumerate(tier.items):
            description = item_description(item)
            for index, line in enumerate(description):
                if index is 0:
                    if item_index is (len(tier.items) - 1):
                        print(prefix + "   └── " + line)
                    else:
                        print(prefix + "   ├── " + line)
                else:
                    if item_index is (len(tier.items) - 1):
                        print(prefix + "       " + line)
                    else:
                        print(prefix + "   │   " + line)
            if isinstance(item.meta_item, gr.Book):
                tier_ratings.append(float(item.meta_item.average_rating))
        ratings += tier_ratings
    average = float(sum(ratings)) / max(len(ratings), 1)
    print("\nAverage rating in bundle: {0:.2f}".format(average))
