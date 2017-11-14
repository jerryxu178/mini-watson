import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
text = "he was a good customer at Mcdonalds and GoodWill"
sents = sent_tokenize(text) # build list of sentences
tokens = word_tokenize(text) # build list of words
tagged_tokens = pos_tag(tokens) # tag tokens
#nltk.help.upenn_tagset('JJ')



from nltk.tag.stanford import StanfordNERTagger

import os
java_path = "C:/Program Files/Java/jdk1.8.0_131/bin/java.exe"
os.environ['JAVA_HOME'] = java_path

st = StanfordNERTagger('stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
					   'stanford-ner/stanford-ner.jar',
					   encoding='utf-8')
classified = st.tag(tokens)


print classified



# NER tagging optional?

def main():
	print "ask me a question"
	while True:
		statement = raw_input(">")
		print generate_response(statement.lower())
		if statement.lower() == "quit":
			break

if __name__ == "__main__":
	main()

