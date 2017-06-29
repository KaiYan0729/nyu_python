#!/usr/bin/env python3
if __name__ == '__main__':
    main()
	
def to_fahrenheit(degrees_celsius):
	degrees_fahrenheit = 9/5* degrees_celsius + 32
    return degrees_celsius

def to_celsius(degrees_fahrenheit):
	degrees_celsius = 5/9*(degrees_fahrenheit - 32)
    return degrees_fahrenheit


import math

def get_fall_time(height):
    # gravity isn't going to change, units in m/(s^2)
    acceleration_by_gravity = 9.8
    time_elapsed = square_root((2 * height) / acceleration_by_gravity)
    return time_elapsed



def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300

    # update this line to calculate time_in_air using get_fall_time() function
	time_in_air = get_fall_time(tower_height)

    tower_range = time_in_air * muzzle_velocity
    
    delta_x = distance(tower_x, target_x)  # difference between tower_x and target_x
    delta_y = distance(tower_y, target_y)  # difference between tower_y and target_y

    separation = square_root(delta_x**2 + delta_y**2)  # the x and y deltas form a triangle, find the hypotenuse
    if separation < tower_range:
        print("The target is closer than the tower range, what should we return?")
        return None
    else:
        print("The target is further than the tower range, what should we return?")
        return None
