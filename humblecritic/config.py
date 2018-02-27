#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

from pathlib import Path

path_to_rc_file = Path.home() / ".humblecriticrc"

# Keys

goodreads_key = "goodreads-developer-key"
goodreads_secret = "goodreads-secret"

# Methods


def entry(key, value):
    return key + "=" + value + "\n"


def setValueFor(key, value):
    if not path_to_rc_file.exists():
        return
    with open(path_to_rc_file, "r") as f:
        config = f.readlines()
    line_number = None
    for num, line in enumerate(config, 0):
        if line.startswith(key):
            line_number = num
    if line_number is None:
        config.append(entry(key, value))
    else:
        config[line_number] = entry(key, value)
    with open(path_to_rc_file, "w") as f:
        f.writelines(config)


def getValueFor(key):
    if not path_to_rc_file.exists():
        return None
    with open(path_to_rc_file, "r") as f:
        config = f.readlines()
    for line in config:
        if line.startswith(key):
            return line.split("=")[1].strip()


def getGoodreadsKeys():
    return {"developer-key": getValueFor(goodreads_key),
            "secret": getValueFor(goodreads_secret)}


def saveGoodreadsKeys(keys):
    setValueFor(goodreads_key, keys["developer-key"])
    setValueFor(goodreads_secret, keys["secret"])
