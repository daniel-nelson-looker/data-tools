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
from bq_anonyize import *

## Can find the names of the methods to use by typing
## faker -h in the terminal or going to https://github.com/joke2k/faker

def main():
	anon = AnonymizeData(file)
	anon = AnonymizeData('/Users/user/Downloads/test.json')
	anon.retrieve_data()
	anon.show_data()
	anon.obfuscate_data(calculation_1 = company_name)
	anon.obfuscate_data(corpus_date=fake.date, corpus=fake.name, word=company_name)
	return

if __name__ == '__main__':
	main()


