import os
import wikipedia
import nltk
from nltk.tag.stanford import StanfordNERTagger

java_path = "C:/Program Files/Java/jdk1.8.0_131/bin/java.exe"
os.environ['JAVA_HOME'] = java_path

st = StanfordNERTagger('stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
					   'stanford-ner/stanford-ner.jar',
					   encoding='utf-8')
#classified = st.tag(tokens)

text = "John Melon is a good worker at Walmart"
sents = nltk.sent_tokenize(text) # build list of sentences
tokens = nltk.word_tokenize(text) # build list of words
tagged_tokens = nltk.pos_tag(tokens) # tag tokens


def search_wikipedia(answer_type, keywords, proper_nouns):
	wiki_pages = []
	for noun in proper_nouns:
		try:
			wiki_pages.append(wikipedia.page(noun))
		except:
			continue

	answers = []
	for page in wiki_pages:
		answers.append(process_page(answer_type, keywords, page))
	return answers

"""
def process_page(answer_type, keywords, page):
	sents = nltk.sent_tokenize(page.content)
	scored_answers = []
	for sentence in sents:
		sent_tokens = nltk.word_tokenize(sentence)
		tagged_sentence = st.tag(sent_tokens)
		score = 0
		answers = []
		for elt in tagged_sentence:
			if elt[0] in keywords:
				score += 1
			if elt[1] == answer_type:
				answers.append(elt[0])
		for ans in answers:
			scored_answers.append((ans, score))
	return scored_answers"""

def generate_NE_dict(answer_type, keywords, page):
	NE_dict = {}
	NER_tagged_page = st.tag(nltk.word_tokenize(page.content))
	curr_entity = "" 
	curr_tag = ""
	for elt in NER_tagged_page:
		if elt[1] != 'O':
			curr_entity += " " + elt[0]
			curr_tag = elt[1]
		else:
			if curr_entity != "":	
				NE_dict[str(curr_entity.strip())] = str(curr_tag)
				curr_entity = ""
				curr_tag = ""
	if curr_entity != "":
		NE_dict[str(curr_entity.strip())] = str(curr_tag)
	return NE_dict


	#tokens = nltk.word_tokenize(page.content)




print process_page("ORGANIZATION", "born", wikipedia.page("Alan Devlin"))
#print st.tag(nltk.word_tokenize((wikipedia.page("Alan Devlin")).content))