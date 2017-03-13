#!usr/bin/env python

#######################################################
# 1. Get Json from BQ
# 2. Map real values to fake values
# 3. Switch Real values with fake values
# 4. insert back into bq
# 
# Take any json file, specify which columns to obfuscate
# and what method to obfuscate with.  Every method builds
# a dictionary to retain analytic value. If you don't do 
# this, you're just randomly swapping stuff out, so a
# COUNT(DISTINCT user_id) would prob be a column of 1's.
#
#######################################################
from customanonymize import *
import sys

## Can find the names of the methods to use by typing
## faker -h in the terminal or going to https://github.com/joke2k/faker


def main():
	mapping_dict = {"word" : company_name, "corpus" : fake.name}
	## Instantiate config object. This will fill in conf with 
	## the values we filled out in bq_anonymize
	conf = ConfigAnon()
	## Extract bq data to gs
	conf.extract_bq_to_gs()
	## Pull in the gs file
	conf.extract_gs_to_local()
	print 'Pulling down Data from Google Cloud Storage to Local'
	## Get the real data attribute to fake data attribute mapping
	## Instantiate anonymization object with a pointer to the
	## json file we just extracted from bq -> gs -> local
	anon = AnonymizeData('output_final.json')
	## Pull the data from local to a python object
	anon.retrieve_data()
	## Can run below for sanity
	# anon.show_data()
	## Do the anonymization work here.
	## This first goes through the data to map real data values
	## to fake ones.  This let's us create profiles.  The second
	## step is replacing the values.
	print 'Anonymizing Data.  This may take a while, so grab a La Croix and Chill.'
	output_file = anon.obfuscate_data(**mapping_dict)
	## Write to local
	output_file_path = open('insert_to_bq.json','w')
	print 'Writing anonymized data to local.  Here is a sample of the anonymized data'
	## Print a sample
	for i in output_file[0:9]:
		print i
	output_file_path.write(str(output_file))
	output_file_path.close()
	return


if __name__ == '__main__':
	main()


