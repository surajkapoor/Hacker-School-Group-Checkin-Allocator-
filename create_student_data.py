import requests
import json
import random
import pdb


checkin_data = {}

def student_data():
	all_student_ids = []
	with open("group.txt") as get_past_groups:
		past_groups = json.loads(get_past_groups.read())
		for group in past_groups:
			for g in group["person_ids"]:
				all_student_ids.append(g)
		all_student_ids = set(all_student_ids)
	with open("student_data.txt", "w") as student_data:	
		for student_id in all_student_ids:
			checkin_data[student_id] = []
			for past_group in past_groups:
				if student_id in past_group["person_ids"]:
					past_group["person_ids"].remove(student_id)
					checkin_data[student_id].extend(past_group["person_ids"])


		checkin_data["all_student_ids"] = list(all_student_ids)	
		student_data.write(json.dumps(checkin_data))			
	return checkin_data


	