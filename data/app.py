#################################################
# Dependencies
#################################################
# Flask (Server)
from flask import Flask, jsonify, render_template, request

# SQL Alchemy(ORM)
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import exc

# Various
import datetime as dt
from random import *
import json
import sys

# Dependencies
import os
import pandas as pd
import numpy as np

###########################################################
# Datbase Setup 
###########################################################
# Connection String
engine = create_engine("sqlite:///data/belly_button_biodiversity.sqlite")

# Reflect DB Contents using SQL Alchemy
Base = automap_base()
Base.prepare(engine, reflect=True)

# Store each table as a class
otu_table = Base.classes.otu
samples_table = Base.classes.samples
metadata_table = Base.classes.samples_metadata

###########################################################
# Flask Setup 
###########################################################
app = Flask(__name__)

###########################################################
# Flask Routes(Web) 
###########################################################


# Basic Testing Route
# ---------------------------------------------------------
@app.route("/")
def basic():
	return("Basic")

# Query Route (otu_table)
# ---------------------------------------------------------
@app.route("/query/otu_table")
def otu_query():
	
	# Connect to the DB
	session = Session(engine)
	
	# Get all otu table
	results = session.query(otu_table)

	#<FILTER>
	#...


	# Specify that I want all the results
	results = results.all()

	# Create list to hold the results
	all_results = []

	# Loop through each record
	for results in results:

		# Create a dictionary
		dict_result = {}
		dict_result["otu_id"] = result.otu_id
		dict_result["lowest_taxonomic_unit_found"] = result.lowest_taxonomic_unit_found

		#Append the individual results into the array
		all_results.append(dict_result)
	
	# Return a json object to the user
	return(jsonify(all_results))

# Query Route (samples_table)
# ---------------------------------------------------------
@app.route("/query/samples")
def samples_query():


#Query Route (metadata_table)
# ---------------------------------------------------------
@app.route("/metadata_table")


###########################################################
# Default App Settings 
###########################################################
if __name__ == "__main__":
	app.run(debug=True)