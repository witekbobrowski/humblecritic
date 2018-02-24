#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import argparse as ap
import humblecritic.humblebundle as hb
import humblecritic.review as review

def setup_parser():
    parser = ap.ArgumentParser()
    parser.add_argument('-l', '--link', help="URL [1 or more] to specific HumbleBundle book bundle.",
                        dest='urls', nargs='*', action='store')
    return parser.parse_args()


def main():
    args = setup_parser()
    for url in args.urls:
        print("Scraping HumbleBundle...")
        bundle = hb.construct_bundle(hb.Builder(url))
        print("Reviewing bundle...")
        results = review.review_bundle(bundle)
        if results is None:
            return
        review.output(bundle, results)


if __name__ == '__main__':
    main()
