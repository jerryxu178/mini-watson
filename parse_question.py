import nltk
import constants
from constants import common_verbs, keyword_tags

def process_question(question):
	"""
	TODO
	"""
	tokens = nltk.word_tokenize(question)
	tagged_tokens = nltk.pos_tag(tokens)
	# use helper functions to parse question here
	answer_type = get_answer_type(question.lower())
	keywords = get_keywords(tagged_tokens)
	proper_nouns = get_proper_n(tagged_tokens)
	# use all other nouns if no proper nouns found
	if len(proper_nouns) == 0:
		sep_keywords = reprioritize_nouns(keywords)
		proper_nouns = sep_keywords[0]
		keywords = sep_keywords[1]
	return (answer_type, keywords, proper_nouns)

def get_answer_type(question):
	"""
	TODO
	"""
	if "who" in question:
		return "PERSON"
	elif "when" in question:
		return "DATE"
	elif "where" in question:
		return "LOCATION"
	else:
		return "ANY"

def get_keywords(tagged_tokens):
	"""
	TODO
	"""
	keywords = []
	for token in tagged_tokens:
		if token[0] not in common_verbs and token[1] in keyword_tags:
			keywords.append(token)
	return keywords

def get_proper_n(tagged_tokens):
	"""
	TODO
	"""
	named_entities = []
	curr_token = ""
	for token in tagged_tokens:	
		if token[1] == "NNP" or token[1] == "NNPS":
			curr_token += " " + token[0]
		else:
			if curr_token != "":
				named_entities.append(curr_token.strip())
				curr_token = ""
	if curr_token != "":
		named_entities.append(curr_token.strip())
	return named_entities

def reprioritize_nouns(tagged_tokens):
	"""
	TODO
	"""
	noun_list = []
	revised_tagged_tokens = []
	for token in tagged_tokens:
		if token[1] == "NN" or token[1] == "NNS":
			noun_list.append(token[0])
		else:
			revised_tagged_tokens.append(token)
	return (noun_list, revised_tagged_tokens)
