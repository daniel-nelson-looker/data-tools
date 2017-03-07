#!usr/bin/env python

#######################################################
#
# Take any json file, specify which columns to obfuscate
# and what method to obfuscate with.  Every method builds
# a dictionary to retain analytic value. If you don't do 
# this, you're just randomly swapping stuff out, so a
# COUNT(DISTINCT user_id) would prob be a column of 1's.
#
#######################################################

import os
from faker import Faker
from customanonymize import *

#Create faker factory
fake = Faker()

# target_file_path = '' 

# input_file = open(input_file,'r')
# real_data = input_file.read()

## kwargs is going to look like
## col1 = faker_method1, ..., colN = faker_methodN
def obfuscate_data(real_data, **kwargs):
	for attribute_to_obfuscate in kwargs.keys():
		fake_methd = kwargs[attribute_to_obfuscate]
		real_fake_map = mapping(real_data, attribute_to_obfuscate, fake_methd)
		for row in real_data:
			row[attribute_to_obfuscate] = real_fake_map[row[attribute_to_obfuscate]]
	return real_data


