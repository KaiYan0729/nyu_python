#!/usr/bin/env python3
import sys
'''
def to_fahrenheit(degrees_celsius):
	degrees_fahrenheit = 9/5 * degrees_celsius + 32
	return degrees_fahrenheit

def to_celsius(degrees_fahrenheit):
	degrees_celsius = 5/9 * (degrees_fahrenheit - 32)
	return degrees_celsius


'''
import math

def get_fall_time(height):
    # gravity isn't going to change, units in m/(s^2)
    acceleration_by_gravity = 9.8
    time_elapsed = math.sqrt((2 * height) / acceleration_by_gravity)
    return time_elapsed



def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
	muzzle_velocity = 300

    # update this line to calculate time_in_air using get_fall_time() function
	time_in_air = get_fall_time(float(tower_height))
	
	tower_range = time_in_air * muzzle_velocity

	delta_x = tower_x - target_x  # difference between tower_x and target_x
	delta_y = tower_y - target_y  # difference between tower_y and target_y

	separation = math.sqrt(delta_x**2 + delta_y**2)  # the x and y deltas form a triangle, find the hypotenuse
	if separation < tower_range:
		print("The target is closer than the tower range.Your encampment is vulnerable")
		return True
	else:
		print("Safe! The target is further than the tower range.")
		return False


def main():
	#degrees_celsius = float(sys.argv[1])
	#print(to_fahrenheit(degrees_celsius))
	#degrees_fahrenheit = float(sys.argv[1])
	#print(to_celsius(degrees_fahrenheit))
	tower_height = float(sys.argv[1])
	tower_x = float(sys.argv[2])
	tower_y = float(sys.argv[3])
	target_x = float(sys.argv[4])
	target_y = float(sys.argv[5])
	print(isVulnerable(tower_height, tower_x, tower_y, target_x, target_y))

if __name__ == '__main__':
    main()