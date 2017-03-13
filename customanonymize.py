#################################################
#
# Put all custom anonymization methods here
# and expose AnonymizeData Class methods.
#
#
#################################################
## Custom lists of anonymous data
from fakecompanylist import *
import sys
from time import gmtime, strftime
import random
from faker import Faker
from anon_conf import *
import json

## Create Faker instance for a bunch of Downstream Operations
fake = Faker()

## Randomly value from custom yeti made fake data lists
def random_value(fakedatalist):
	return random.choice(fakedatalist)


## Checking to make sure we have enough fake data
## Assuming that real data is an arraw of 1 dimensional json
def enough_fake_data(real_data,fake_data):
	real_data_size = len(real_data)
	fake_data_size = len(fake_data)
	if real_data_size > fake_data_size:
		print 'Not enough random values'
		syslog.syslog(syslog.LOG_ERR, "Not enough fake values to fill the data in, get more fake data for this" + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	return



## Faker method for this sucked so here we are
## I hardcoded the fakecompanies list in the args.
## Didn't really seem like a reason to paramaterize
## that, other wise it would be x_name or something
def company_name():
	fake_rand = random_value(fakecompanies)
	return fake_rand
	

#######################################################
#
# Take any json file, specify which columns to obfuscate
# and what method to obfuscate with.  Every method builds
# a dictionary to retain analytic value. If you don't do 
# this, you're just randomly swapping stuff out, so a
# COUNT(DISTINCT user_id) would prob be a column of 1's.
#
#######################################################
## Want dictionary where keys are the real 
## data values and the values are the 
## anonymized data.

## Can find the names of the methods to use by typing
## faker -h in the terminal or going to https://github.com/joke2k/faker

def mapping(real_data, col_name, fake_meth):
	final_mapping = {}
	unique_values = set([])
	for row in real_data:
		unique_values.add(row[col_name])
	real_values = list(unique_values)
	for value in real_values:
		final_mapping[value] = fake_meth()
	return final_mapping
 


## Use this class to anonymize the data.  Should only ever
## to pass 1 arguments, the file path to the json file
# 
# 
## Example of this
# anon = AnonymizeData(file)
# anon.retrieve_data()
# anon.show_data()
# anon.obfuscate_data(calculation_1 = company_name)


class AnonymizeData(object):
	def __init__(self,datafile):
		self.datafile = datafile
#
	def retrieve_data(self):
		inputf = open(self.datafile,'r')
		input_file = inputf.read()
		## Since BQ returns new line delimited json,
		## going to loop through each line and make into
		## a proper json object
		self.datafile = []
		for jobj in input_file.splitlines():
			u = json.loads(jobj)
			self.datafile.append(u)
		return self.datafile
# 
	## Show first ten rows of data for sanity
	def show_data(self):
		for row in self.datafile[0:9]:
			print row
		return
# 
	## This is the function that switches the real data with the 
	## fake data
	## kwargs is going to look like
	## col1 = faker_method1, ..., colN = faker_methodN
	def obfuscate_data(self, **kwargs):
		# 
		for attribute_to_obfuscate in kwargs.keys():
			fake_methd = kwargs[attribute_to_obfuscate]
			real_fake_map = mapping(self.datafile, attribute_to_obfuscate, fake_methd)
			# 
			for row in self.datafile:
				row[attribute_to_obfuscate] = real_fake_map[row[attribute_to_obfuscate]]
				# 
		return self.datafile



## Don't touch this unless the configuration changes.
## This allows the end user to fill out the bq_anonymize.conf
## file and just run one script
class ConfigAnon(object):
# 	
	def __init__(self):
		self.google_storage_bucket = google_storage_bucket
		self.bq_destination_file = bq_destination_file
		self.bq_project = bq_project
		self.bq_dataset = bq_dataset
		self.bq_table = bq_table
# 
		self.bq_object = bq_project + ":" + bq_dataset + "." + bq_table
		self.gs_uri = "gs://" + google_storage_bucket + "/" + bq_destination_file
# 
# 
# 
# 
# 
	def make_bq_extract(self):
		bq_extract = 'bq extract --destination_format=NEWLINE_DELIMITED_JSON ' + "'"  + bq_object  + "' " + gs_uri
		return bq_extract
# 
	def extract_bq_to_gs(self):
		bq_extract = self.make_bq_extract()
		return os.system(bq_extract)
# 
	def extract_gs_to_local(self):
		gs_extract = 'gsutil cat ' + gs_uri + ' > output_final.json'
		return os.system(gs_extract)
# 
	def bring_in_column_mapping(self):
		return mapping_dict






