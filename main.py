from parse_question import process_question
from wiki_search import search_wikipedia
from process_answers import prepare_answers

def main():
	"""
	TODO
	"""
	print "Hello! Please ask me a question"
	while True:
		question = raw_input(">")		
		(answer_type, keywords, proper_nouns) = process_question(question)
		if len(proper_nouns) == 0:
			# no proper or common nouns found in the question
			print "I don't understand question's subject, please try again"
			continue
		scored_answers = search_wikipedia(answer_type, keywords, proper_nouns)
		answer_list = prepare_answers(scored_answers, question)
		if len(answer_list) == 0:
			# searching Wikipedia yielded no results
			print "No potential answers found"
			continue
		print "Is the answer " + answer_list[-1] + "? [y/n]"
		reply = raw_input(">")
		if reply == "y":
			print "Great!"
		elif reply == "n":
			if len(answer_list) > 1:
				print "Here were my other guesses: " + str(answer_list[:-1])[1:-1]
			else:
				print "Hmm... I am stumped!"
		else:
			print "Unexpected response, I was expecting 'y' or 'n'"
		print "Please feel free to ask me another question"

if __name__ == "__main__":
	main()

