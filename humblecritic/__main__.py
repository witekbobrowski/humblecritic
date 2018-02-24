#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import humblecritic.humblebundle as hb
import humblecritic.review as review
import humblecritic.utils as utils


def main():
    args = utils.setup_parser()
    bundles = []
    if args.urls != None:
        for url in args.urls:
            print("Scraping HumbleBundle...")
            bundle = hb.construct_bundle(hb.Builder(url))
            print("Reviewing bundle...")
            review.review_bundle(bundle)
            bundles.append(bundle)
            utils.print_summary(bundle)
    if args.json_file != None:
        print("Exporting to " + args.json_file + "...")
        utils.export_to_json(args.json_file, bundles)


if __name__ == '__main__':
    main()
