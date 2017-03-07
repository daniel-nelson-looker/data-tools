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


## Instructions:
## 1. Create an instance of AnonymizeData with path to datafile 
##    ie. anon = AnonymizeData('gadata.json')
## 2. Call anon.retrieve_data() to get data file.
## 3. Call obfuscate_data to anonymize data

class AnonymizeData(object):
	def __init__(self, datafile):
		self.datafile = datafile
	def retrieve_data(datafile):
		input_file = open(datafile,'r')
		print "found file"
		real_data = input_file.read()
		return real_data
# 
	## kwargs is going to look like
	## col1 = faker_method1, ..., colN = faker_methodN
	def obfuscate_data(real_data, **kwargs):
		for attribute_to_obfuscate in kwargs.keys():
			fake_methd = kwargs[attribute_to_obfuscate]
			real_fake_map = mapping(real_data, attribute_to_obfuscate, fake_methd)
			for row in real_data:
				row[attribute_to_obfuscate] = real_fake_map[row[attribute_to_obfuscate]]
		return real_data

anon = AnonymizeData('rv.json')

