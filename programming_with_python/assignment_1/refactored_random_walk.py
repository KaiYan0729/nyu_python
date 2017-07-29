#!/usr/bin/env python3

import random
import sys
import math

def get_random_direction():
	direction = ""
	probability = random.random()

	if probability < 0.25:
		direction = "west"
		displacements = (-1, 0)
	elif probability >= 0.25 and probability < 0.5:
		direction = "east"
		displacements = (1, 0)
	elif probability >= 0.5 and probability < 0.75:
		direction = "north"
		displacements = (0, 1)
	else:
		direction = "south"
		displacements = (0, -1)
	#return direction
	return displacements

def take_all_walks(steps, runs):
	endpoints = []
	for run_index in range(runs):
		current_location = [0, 0]
		for step_index in range(steps):
			displacement = get_random_direction()
		# extract the numerical values from the tuple
			delta_x = displacement[0]
			delta_y = displacement[1]

		# UPDATE current_location HERE
			current_location[0] += delta_x
			current_location[1] += delta_y
		end_location = current_location
		
		endpoints.append(end_location)
	return endpoints

def average_final_distance(endpoints):
	total_distance = 0
	for coords in endpoints:
		dx = coords[0]
		dy = coords[1]
		
		# use the Pythagorean theorem to get distance like last session
		distance = math.sqrt(dx*dx + dy*dy)

		total_distance += distance

	return total_distance / len(endpoints)

if __name__ == "__main__":
	steps = 10
	if len(sys.argv) > 1:
		steps = int(sys.argv[1])
		
	runs = 50
	if len(sys.argv) > 2:
		runs = int(sys.argv[2])
	
	end_locations = take_all_walks(steps, runs)

	print("Done with walk, printing end location: ")
	print(end_locations)

	average_displacement = average_final_distance(end_locations)
	print('Average displacement is: ')
	print(average_displacement)