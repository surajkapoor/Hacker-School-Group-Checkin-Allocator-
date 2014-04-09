from create_student_data import student_data
from collections import Counter
import random
import sys

shuffled_groups = {}


class Groups(object):


	def __init__(self):
		self.locations = {"Lovelace" : 6, "Russell" : 6, "Babbage" : 6, "Von Neumann" : 5, "Dijkstra" : 5, "Turing" : 6, "Ritchie" : 6, "Hopper" : 5, "Church" : 5, "McCarthy" : 5}
		self.possible_new_group = {}
		self.overlap_counter = 0


	def generate_new_groups(self, student_ids = student_data()["all_student_ids"]):	
		random.shuffle(student_ids)
		start = 0
		end = 0
		for location in self.locations:
			end += self.locations[location]
			self.possible_new_group[location] = student_ids[start:end] 
			start = end
		return

	def _create_score(self, l1, l2):
		count = Counter([val for val in l2 if val in l1])
		for i in count:
			self.overlap_counter += 10 ** count[i]	


	def overlap_count(self, student_data = student_data()):
		self.generate_new_groups()
		for new_group in self.possible_new_group.keys():
			for each_student_in_group in self.possible_new_group[new_group]:
				self._create_score(self.possible_new_group[new_group], student_data[each_student_in_group])
		return


def main(n):
	counter = 0
	while counter < n:
		g = Groups()
		g.overlap_count()
		shuffled_groups[g.overlap_counter] = g.possible_new_group
		counter += 1
	optimal_group_config = min(shuffled_groups.keys())
	return shuffled_groups[optimal_group_config], "overlap score == {0}".format(optimal_group_config)


if __name__ == "__main__":
 	if len(sys.argv) == 1:
 		print main(10)	
 	elif len(sys.argv) == 2:
 		try:
 			number_of_shuffles = int(sys.argv[1])
 		except ValueError:
 			print "argument should be an integer"
 			number_of_shuffles = raw_input("enter a value:")
 		print main(number_of_shuffles)
 	else:
 		print "incorrect command"	


		