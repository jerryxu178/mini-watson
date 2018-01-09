# all constants for mini-watson here

# common question words that determine what the question is asking for
question_words = ["who", "what", "when", "where"]

# words with the listed POS tags are to be considered as keywords
keyword_tags = ["CD", "JJ", "JJR", "JJS", "NN", "NNS", "PDT", "RB", "RBR", 
"RBS", "RP", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

# common verbs are not to be used as keywords
common_verbs = ["is", "are", "was", "were", "am", "are"]

# option to combine similar potential answers
# the answers "New York" and "New York City" would have their scores combined
# and the resulting answer will simply be "New York City", for better or worse
combine_answers = True