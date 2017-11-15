
def prepare_answers(scored_answers, question):
	filtered_answers = remove_unwanted_ans(scored_answers, question)
	filtered_answers = combine_duplicate_ans(filtered_answers)
	filtered_answers.sort(key=lambda ans: ans[1]) 
	answers = []
	for elt in filtered_answers:
		answers.append(elt[0])
	return answers


def remove_unwanted_ans(scored_answers, question):
	filtered_answers = []
	for answer in scored_answers:
		if answer[1] != 0 and answer[0] not in question:
			filtered_answers.append(answer)
	return filtered_answers

def combine_duplicate_ans(scored_answers):
	answers_dict = {}
	for answer in scored_answers:
		if answer[0] in answers_dict:
			answers_dict[answer[0]] += answer[1]
		else:
			answers_dict[answer[0]] = answer[1]
	ans_list = []
	for ans in answers_dict:
		ans_list.append((ans, answers_dict[ans]))
	return ans_list