#!usr/bin/env python
#################################################
#
# Config File for script
# 
#
#
#################################################
import os
from customanonymize import *

google_storage_bucket = 'harvest-143322.appspot.com'
bq_destination_file = 'test.json'
bq_project = 'publicdata'
bq_dataset = 'samples'
bq_table = 'shakespeare'
#
#
# making table references and google cloud storage uri
bq_object = bq_project + ":" + bq_dataset + "." + bq_table
gs_uri = "gs://" + google_storage_bucket + "/" + bq_destination_file
#
#
# real data attribute to fake data mapping
# 
