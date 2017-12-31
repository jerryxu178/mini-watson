# Watson-lite
Watson-lite takes your trivia questions and answers them using the wisdom of Wikipedia. 

## Getting Started

### Prerequisites
To run Watson-lite, you will need the following:
-Python 2.7
-NLTK
-Stanford NER tagger??
-Git (recommended)

### Running trivia-bot
Open the command prompt and, from a directory of your choosing, run the 
following commands:

1. git clone https://github.com/jerryxu178/trivia-bot.git
2. cd trivia-bot
3. python main.py

## Screenshots

### Questions that work

![April 1492](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot1.jpg?raw=true "when did Christopher Columbus sail the ocean blue?")  

![Columbus](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot2.jpg?raw=true "where is the capital of Ohio?")  

![Vincent van Gogh](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot3.jpg?raw=true "who painted Starry Night?")  

### Questions that don't work

![Natalie Babbitt](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot4.jpg?raw=true "who is the author of Tuck Everlasting?")  
The author of Tuck Everlasting is Natalie Babbitt, Winnie Foster is actually the protagonist.

![New York City](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot5.jpg?raw=true "where is the Freedom Tower?")  
This is a fairly open-ended question, but the answer is obviously wrong.  
However, if we tweak the question slightly...

![New York City](https://github.com/jerryxu178/watson-lite/blob/master/screenshots/screenshot6.jpg?raw=true "Where is the Freedom Tower located?")  

## Acknowledgements