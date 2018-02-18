# humblecritic

<p align=center>
<a href="">
<img alt="" src="https://img.shields.io/badge/python-v3.6.3-blue.svg">
</a>
</p>

💯 Get score for HumbleBundle bundle

#### Bundles supported:

- [x] Book bundle (ratings from [Goodreads](goodreads.com))
- [ ] Game bundle
- [ ] Software bundle
- [ ] Mobile bundle

## Usage

Before running make sure you have all dependencies installed
```
$ pip3 install -r requirements.txt
```
then head over to [\_\_main\_\_.py](humble_rating/\_\_main\_\_.py) and pass Goodreads developer key and secret
```
client = gr.GoodreadsClient("dev-key", "secret")
```
run the script
```
$ python3 humblecritic --url https://www.humblebundle.com/books/functional-programming-books
```

## Contents

I've tried to break down the logic to modules so I can easily extend the functionality in the future (ex. by supporting game bundles and getting reviews from metacritic.com).
```
.
├── LICENSE
├── README.md
├── humble_rating
│   ├── __init__.py
│   ├── __main__.py
│   ├── goodreads
│   │   ├── __init__.py
│   │   ├── book.py
│   │   └── client.py
│   └── humblebundle
│       ├── __init__.py
│       ├── builder.py
│       ├── bundle.py
│       ├── item.py
│       ├── scraper.py
│       └── tier.py
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
- [ ] Cleanup repo and code refinements before public GitHub release
- [ ] Game/Mobile Bundles support
