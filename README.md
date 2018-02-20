<p align=center>
<a href="">
<img height=180 alt="" src="logo.png">
</a>
</p>
<p align=center>
<a href="">
<img alt="" src="https://img.shields.io/badge/python-v3.6.3-blue.svg">
</a>
</p>

💯 Get score for HumbleBundle bundle

# Bundles supported:

- [x] Book bundle (ratings from [Goodreads](goodreads.com))
- [ ] Game bundle
- [ ] Software bundle
- [ ] Mobile bundle

## Installation

Clone this repository and from the project directory run install.sh

```
$ ./install.sh
```

And thats basically it.

Note: To access some services (like goodreads) the scripts needs to have api keys. You will be promped to pass these in if needed.

## Usage

The installation process will supply entry point for the script so you can run it like so

```
$ humblecritic -l https://www.humblebundle.com/books/functional-programming-books
```

## Contents

I've tried to break down the logic to modules so I can easily extend the functionality in the future (ex. by supporting game bundles and getting reviews from metacritic.com).

```
.
├── LICENSE
├── README.md
├── humble_rating
│   ├── __init__.py
│   ├── __main__.py
│   ├── goodreads
│   │   ├── __init__.py
│   │   ├── book.py
│   │   └── client.py
│   └── humblebundle
│       ├── __init__.py
│       ├── builder.py
│       ├── bundle.py
│       ├── item.py
│       ├── scraper.py
│       └── tier.py
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── context.py
    ├── goodreads_test.py
    └── humblebundle_test.py
```

## TODO

- [ ] Enhance output
- [ ] Nicer README
- [ ] Add config
- [ ] Add options (ex. --charity - to show which charity bundle supports)
- [ ] Cleanup repo and code refinements before public GitHub release
- [ ] Game/Mobile Bundles support
