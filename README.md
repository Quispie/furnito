#Furnito

##Contents

+ [Intro](#intro)
+ [Business](#business)
+ [Inrerface](#interface)
+ [Crawler](#crawler)
+ [Pre-process]
+ [Indexing]
+ [Ranking]
+ [Evaluation]
+ [Furture]

<h2 id='intro'>Intro</h2>

<h2 id='business'>Business</h2>

<h2 id='interface'>Interface</h2>

<h2 id='crawler'>Crawler</h2>

The goal of our web crawler is to access data *quickly*, *efficiently* and as many *useful resources* as possible. As our target site is [overstock](http://www.overstock.com/) — a furniture website, we need to crawl as many furnitures as possible, so the design of crawler is respect to *breath first strategy*. Here is a short description of different modules of our crawler:

1. config module, record all user configurable settings, including `base_url`, `depth`, `data_path` etc.
2. initial module, initial a  classes and libraries we need to use. As we are using python for the whole project, the initial module is written in `__init__.py`.
3. field module, decide for a specific furniture, which field of data do we nedd to crawl. For our case, furniture `name`, `price`, `description`, `reviews` and `origin_link` are the most important properties.
4. crawl module, using *Xpath* extractor to extract useful field for a given furniture url.
5. url manager, manage url, include several functions including `add_url`, `remove_url` and `history_url`. This module is used for interact with module *URL_POOL*.
6. url pool, manage url in a queue data structure, and ensure there is no duplicate url exist.
7. robot module, use to read *Robot.txt* and decide crawl strategy.
8. log module, use to recode error in order to keep crawler robust.

Use `config.py` to config your personal settings, run `start.py` to start crawl. Library dependency: `lxml` and `requests`.