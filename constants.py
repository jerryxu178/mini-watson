# all constants for trivia-bot here

# common question words that determine what the question is asking for
question_words = ["who", "what", "when", "where"]

# words with the listed POS tags are to be considered as keywords
keyword_tags = ["CD", "JJ", "JJR", "JJS", "NN", "NNS", "PDT", "RB", "RBR", 
"RBS", "RP", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

# common verbs are not to be used as keywords
common_verbs = ["is", "are", "was", "were", "am", "are"]