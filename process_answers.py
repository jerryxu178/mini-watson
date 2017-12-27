import constants

# answer retrieval for watson-lite

def prepare_answers(scored_answers, question):
	"""
	Combine any similar or duplicate answers in the scored_answers list, and
	also remove any answers that are already stated in the question or have a 
	score of 0. 

	Return a list of answers sorted by score in descending order
	"""
	filtered_answers = remove_unwanted_ans(scored_answers, question)
	filtered_answers = combine_duplicate_ans(filtered_answers)
	if constants.combine_answers:
		filtered_answers = combine_similar_answers(filtered_answers)
	filtered_answers.sort(key=lambda ans: ans[1]) 
	answers = []
	for elt in filtered_answers:
		answers.append(elt[0])
	return answers


def remove_unwanted_ans(scored_answers, question):
	"""
	Remove any answers that have a score of 0 or are already stated in the 
	question
	"""
	filtered_answers = []
	for answer in scored_answers:
		if answer[1] != 0 and answer[0] not in question:
			filtered_answers.append(answer)
	if len(filtered_answers) == 0:
		return scored_answers
	return filtered_answers

def combine_duplicate_ans(scored_answers):
	"""
	Combine scores for answers that are identical
	"""
	answers_dict = {}
	for answer in scored_answers:
		if answer[0] in answers_dict:
			if answer[1] == 0:
				answers_dict[answer[0]] += 1
			else:
				answers_dict[answer[0]] += answer[1]
		else:
			if answer[1] == 0:
				answers_dict[answer[0]] = 1
			else:
				answers_dict[answer[0]] = answer[1]
	ans_list = []
	for ans in answers_dict:
		ans_list.append((ans, answers_dict[ans]))
	return ans_list

def combine_similar_answers(scored_answers):
	"""
	Combine scores for answers that are similar
	i.e. "New York" and "New York City" will have their scores combined and 
	the corresponding answer would just be "New York City"
	"""
	for ans in scored_answers:
		for other_ans in scored_answers:
			if ans[0] != other_ans[0] and ans[0] in other_ans[0]:
				scored_answers.append((other_ans[0],other_ans[1] + ans[1]))
				try:
					scored_answers.remove(ans)
				except ValueError: 
					pass
				try:
					scored_answers.remove(other_ans)
				except ValueError: 
					pass
	return scored_answers