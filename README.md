#Furnito

##Contents

+ [Intro](#intro)
+ [Business](#business)
+ [Inrerface](#interface)
+ [Crawler](#crawler)
+ [Tokenize]
+ [Indexing]
+ [Ranking]
+ [Evaluation]
+ [Furture]

<h2 id='intro'>Intro</h2>

<h2 id='business'>Business</h2>
Business process model 
![BPMN model](https://github.com/Informationretrieval2016/furnito/blob/master/img/Schermafbeelding%202016-03-18%20om%2011.35.29.png "BPMN model")

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

<h2 id='tokenize'>Tokenize</h2>

<h2 id='indexing'>Indexing</h2>

The general introduction of how to build an *Inverted Index* can be found [here](http://nlp.stanford.edu/IR-book/information-retrieval-book.html). In **Furnito**, we implemented an simple *inverted index* which contains two parts: first part is *dict* and the second part is a *posting list*. Below I'd like to introduce these two parts separately.

**Dictionary** is a part allow query to quickly access where is the current document storage, this part need to be store in memory. For most cases, **Dictionary** need to be store in *hashtable*, in python, we use *dict*. The data structure of our Dictionary looks like this:

| index | term   |
| ----- | ------ |
| 0     | aero   |
| 1     | bed    |
| ...   | ...    |
| n     | yellow |

As shown in table, we gave each term an *index*, and different terms a sorted alphabetically. In order to avoid memory overload, we done this task by the following steps:

1. collect `term`,  `doc_name` from 1 furniture document, write to temp file.
2. collect the same fileds from the second document and pair-wise merge two list of terms.
3. loop through all other furniture documents and do the same thing.
4. use `defaultdict` of python to reduce data according to term, get result like this: `{term: [doc1, doc3, doc7]}`, where term is the sorted term, list of doc indicates in which documents the current term appears.
5. Construct **Dictionary** by adding a int index, store in memory.
6. Construct **Pooling List** by replace all terms by index defined before, export to local storage.

Finall Inverted Index looks like this:

![posting-list](img/posting_list.png)
