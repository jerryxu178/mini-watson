# Mini-Watson
Mini-Watson takes your trivia questions and answers them using the wisdom of Wikipedia. 
## Screenshots
### Answering questions correctly

![April 1492](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot1.jpg?raw=true "when did Christopher Columbus sail the ocean blue?")  

![Columbus](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot2.jpg?raw=true "where is the capital of Ohio?")  

![Vincent van Gogh](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot3.jpg?raw=true "who painted Starry Night?")  

### Answering questions incorrectly

![Natalie Babbitt](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot4.jpg?raw=true "who is the author of Tuck Everlasting?")  
The author of Tuck Everlasting is Natalie Babbitt, Winnie Foster is actually the protagonist.

![New York City](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot5.jpg?raw=true "where is the Freedom Tower?")  
This is a fairly open-ended question, but the answer is obviously wrong.  
However, if we tweak the question slightly...

![New York City](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot6.jpg?raw=true "Where is the Freedom Tower located?")  

## Running Mini-Watson
From the directory containing the installation of Mini-Watson, simply run
```python
python main.py
```
### Prerequisites
Running Mini-Watson requires NLTK, Stanford NER, and the wikipedia Python library in addition to the base code.

#### NLTK
The Natural Langauge Tooklkit (NLTK) is useful for tokenizing text and identifying parts of speech. The installation instructions can be found [here](http://www.nltk.org/install.html).

#### Stanford NER
The instructions for installing Named Entity Recognition (NER) can be found [here](https://nlp.stanford.edu/software/CRF-NER.shtml). 
Note: the environment variables may need to be set in wiki_search.py

#### wikipedia
Mini-Watson uses the wikipedia 1.4.0 Python library. The installation instructions can be found [here](https://pypi.python.org/pypi/wikipedia/).
