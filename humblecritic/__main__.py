#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from humblecritic import humblebundle as hb
from humblecritic import review as review
from humblecritic import utils as utils


def main():
    args = utils.setup_parser()
    bundles = []
    if args.urls is not None:
        for url in args.urls:
            print("Scraping HumbleBundle...")
            bundle = hb.construct_bundle(hb.Builder(url))
            print("Reviewing bundle...")
            review.review_bundle(bundle)
            bundles.append(bundle)
            utils.print_summary(bundle)
    if args.json_file is not None:
        utils.export_to_json(args.json_file, bundles)
        print("Exported scraped data to '" + args.json_file + "'.")


if __name__ == '__main__':
    main()
