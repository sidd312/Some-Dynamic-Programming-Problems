#!/usr/bin/python

def maxcontiguoussubsequence(input_list, start_index, end_index):
	"""Find the maximum contiguous sum from a given input list using Kadane's algorithm"""

	max_so_far = 0
	max_ending_here = 0
	#Check if all negative numbers are there in the list
	if (checkfornegative(input_list, start_index, end_index)):
		return max(input_list)
	
	else:
	#Loop through the list and find the maximum contiguous subsequence sum
	    for num in xrange(start_index,end_index + 1):
			max_ending_here = max_ending_here + input_list[num]
			if (max_ending_here < 0):
				max_ending_here = 0

			elif (max_so_far < max_ending_here):			
					max_so_far = max_ending_here
	return max_so_far

def checkfornegative(templist,start_index, end_index):
	"""Checks for all negative numbers in the list"""
	negative_checker = True
	
	for num in xrange(start_index,end_index + 1):
		if templist[num] >= 0:
			negative_checker = False
	return negative_checker 

if __name__ == "__main__":
	usr_input = raw_input("Enter a list of numbers: ")
	input_list = map(int, usr_input.split())
	list_range = raw_input("Enter the range : ")
	(start_index,end_index) = map(int, list_range.split()) 
	print "Maximum contiguous subsequence sum is:" + str(maxcontiguoussubsequence(input_list,start_index-1,end_index-1))


