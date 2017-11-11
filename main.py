import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
text = "Machine learning is Michael Scott the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI."
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
