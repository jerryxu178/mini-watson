import nltk
import constants
from constants import common_verbs, keyword_tags

def process_question(question):
	"""
	Parse the question string to retrieve the keywords and proper nouns that
	are in the question, and also determine the appropriate type of answer
	(person, date, etc.) needed
	"""
	tokens = nltk.word_tokenize(question)
	tagged_tokens = nltk.pos_tag(tokens)
	# use helper functions to parse question here
	answer_type = get_answer_type(question.lower())
	keywords = get_keywords(tagged_tokens)
	proper_nouns = get_proper_n(tagged_tokens)
	# use common nouns if no proper nouns found
	if len(proper_nouns) == 0:
		sep_keywords = reprioritize_nouns(keywords)
		proper_nouns = sep_keywords[0]
		keywords = sep_keywords[1]
	return (answer_type, keywords, proper_nouns)

def get_answer_type(question):
	"""
	Return "PERSON" if question asks who
	Return "DATE" if question asks when
	Return "LOCATION" if question asks where
	Otherwise return "ANY"
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
	Retrieves keywords from POS tagged question
	Keywords are nouns, verbs, and other important parts of speech. Common
	verbs such as "was" and "were" are ignored

	Returns a list of keywords
	"""
	keywords = []
	for token in tagged_tokens:
		if token[0] not in common_verbs and token[1] in keyword_tags:
			keywords.append(token)
	return keywords

def get_proper_n(tagged_tokens):
	"""
	Retrieves all proper nouns from question, and returns them in a list
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
	If no proper nouns are found in the question, use this function to retrieve
	all other common nouns that are in the question

	Will try to find wiki pages of common nouns later on, since no proper nouns
	are available
	"""
	noun_list = []
	revised_tagged_tokens = []
	for token in tagged_tokens:
		if token[1] == "NN" or token[1] == "NNS":
			noun_list.append(token[0])
		else:
			revised_tagged_tokens.append(token)
	return (noun_list, revised_tagged_tokens)
