#################################################
#
# Put all custom anonymization methods here
#
#################################################
## Custom lists of anonymous data
from fakecompanylist import *
import sys
from time import gmtime, strftime
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
	return random.sample(fakedatalist,len(fakedatalist))




## Checking to make sure we have enough fake data
## Assuming that real data is an arraw of 1 dimensional json
def enough_fake_data(real_data,fake_data):
	real_data_size = len(real_data)
	fake_data_size = len(fake_data)
	if real_data_size > fake_data_size:
		print 'Not enough random values'
		syslog.syslog(syslog.LOG_ERR, "Not enough fake values to fill the data in, get more fake data for this" + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
		return



## Map 1 column to list of fake names
## need to know the column they want to map to
## once this is used, I'm assuming that the data has 
## been randomized, correctly selected, and that there
## is enough fake data to proceed. Also assuming that data
## is an array of 1 dimensional json, and the fake data 
## is a list 
def company_name(real_data, fake_data):
	## Making a set to get UNIQUE values of the data
	## then building a list so I can build a dictionary
	## mapping real values to fake values.  This will also
	## allow profiling later. 
	unique_values = set([])

	for row in real_data:
		unique_values.add(row[attribute_name])

	real_values = list(unique_values)
	fake_values = fakecompanies
	data_mapping = {}

	for value in real_values:
		data_mapping[value] = fake_values[0]
		del fake_values[0]

	return data_mapping
















