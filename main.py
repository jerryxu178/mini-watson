import nltk #remove this?
from parse_question import process_question
from wiki_search import search_wikipedia
from process_answers import prepare_answers
"""
text = "John Melon is a good worker at Walmart"
sents = nltk.sent_tokenize(text) # build list of sentences
tokens = nltk.word_tokenize(text) # build list of words
tagged_tokens = nltk.pos_tag(tokens) # tag tokens
#nltk.help.upenn_tagset('JJ')



# NER tagging optional?
from nltk.tag.stanford import StanfordNERTagger

import os
java_path = "C:/Program Files/Java/jdk1.8.0_131/bin/java.exe"
os.environ['JAVA_HOME'] = java_path

st = StanfordNERTagger('stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
					   'stanford-ner/stanford-ner.jar',
					   encoding='utf-8')
classified = st.tag(tokens)

print classified
"""
 
def main():
	print "ask me a question"
	while True:
		question = raw_input(">")		
		(answer_type, keywords, proper_nouns) = process_question(question)
		if len(proper_nouns) == 0:
			print "no subjects found in question, please try again"
			continue
		scored_answers = search_wikipedia(answer_type, keywords, proper_nouns)
		answer_list = prepare_answers(scored_answers, question)
		if len(answer_list) == 0:
			print "no potential answers found"
			continue
		print "Is the answer " + answer_list[0] + "? [y/n]"
		reply = raw_input(">")
		if reply == "y":
			print "great!"
		elif reply == "n":
			if len(answer_list) > 1:
				print "Here were my other guesses: " + str(answer_list[1:])
			else:
				print "no other guesses"
		else:
			print "unexpected response, was expecting 'y' or 'n'"
		print "\nfeel free to ask another question"

if __name__ == "__main__":
	main()

