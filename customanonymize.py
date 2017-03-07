#################################################
#
# Put all custom anonymization methods here
#
#################################################
## Custom lists of anonymous data
from fakecompanylist import *
import sys
from time import gmtime, strftime
import random

## Want to make a service that allows people to
# 1. specify what columns to obfuscate
# 2. pick what database / project / table to insert into
# 3. scale numeric data and add some exogeniety to it
# 4. change strings to specic types of data, ie. company name

## Going to borrow us many methods from faker as possible

## TODO
# 1. Allow profiles. This would keep emails and stuff 
#    consistent. 
# 2. Have a webservice that provides a gui for this



## Randomly order fake data
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
## tha, other wise it would be x_name or something
def company_name():
	fake_rand = random_value(fakecompanies)
	return fake_rand
	

## Want dictionary where keys are the real 
## data values and the values are the 
## anonymized data.
def mapping(real_data, col_name, fake_meth):
	final_mapping = {}
	unique_values = set([])
	for row in real_data:
		unique_values.add(row[col_name])
	real_values = list(unique_values)
	for value in real_values:
		final_mapping[value] = fake_meth()
	return final_mapping

 



1. Get Json from BQ
2. Map real values to fake values
3. Switch Real values with fake values
4. insert back into bq







