import os
import wikipedia
import nltk
from nltk.tag.stanford import StanfordNERTagger

java_path = "C:/Program Files/Java/jdk1.8.0_131/bin/java.exe"
os.environ['JAVA_HOME'] = java_path

st = StanfordNERTagger('stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
					   'stanford-ner/stanford-ner.jar',
					   encoding='utf-8')

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
	contents = page.content
	contents = contents.encode('ascii', 'ignore')
	contents = contents.replace("\n", "")
	contents = contents.replace("=", "")



	NER_tagged_page = st.tag(nltk.word_tokenize(contents))
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
def process_page(answer_type, keywords, page):
	NE_dict = generate_NE_dict(answer_type, keywords, page)
	sentences = []
	encountered_NE = []
	for NE in NE_dict:
		if NE_dict[NE] == answer_type or answer_type == "ANY":
			contents = page.content
			contents = contents.encode('ascii', 'ignore') # contents = contents.encode('ascii', 'replace') 
			contents = contents.replace("\n", "")
			contents = contents.replace("=", "")


			sentences += [s + '.' for s in (contents).split('.') if NE in s]
			encountered_NE.append(NE)
	sentences = list(set(sentences))
	scored_answers = []
	for sent in sentences:
		score = 0
		for word in keywords:
			if word[0] in sent:
				score += 1
		for NE in encountered_NE:
			if NE in sent:
				scored_answers.append((NE, score))
	scored_answers.sort(key=lambda ans: ans[1])
	return scored_answers



# print process_page("LOCATION", "born", wikipedia.page("Alan Devlin"))
#print st.tag(nltk.word_tokenize((wikipedia.page("Alan Devlin")).content))