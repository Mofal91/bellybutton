<<<<<<< HEAD
###########################################################
# Dependencies
###########################################################
# Flask(Server)
from flask import Flask, jsonify, render_template, request
import json

# SQL Alchemy(ORM)
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Dependencies
import os
import pandas as pd
import numpy as np

###############################################################
# Flask Setup 
###############################################################
app = Flask(__name__)
###############################################################
# Database Setup
###############################################################
dbfile = os.path.join('db', 'belly_button_biodiversity.sqlite')
engine = create_engine(f"sqlite:///{dbfile}")

#Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each Table
Samples_Metadata = Base.classes.samples_metadata
OTU = Base.classes.otu
Samples = Base.classes.samples

# Create our session(link)
session = Session(engine)

###########################################################
# Flask Route
###########################################################
@app.route("/")
def index():
	"""Return the homepage."""
	return render_template('index.html')

@app.route("/names")
def names():
	"""List of sample names.
	Returns a
	[
		"BB_940",
		"BB_941",
		"BB_944",
		"BB_945",
		"BB_946",
		"BB_947",
		...
	]
	"""
	#Use Pandas to perform the sql query
	stmt = session.query(Samples).statement
	df = pd.read_sql_query()
	df.set_index()

	# Return a list of the column names (sample names)
	return jsonify(list(df.columns))

@app.route('/otu')
def otu():
	"""List of OTU descriptions.
	Returns a list of OTU descriptions in the following format
	[
		"Archaea;Euryarchaeota;Halobacteria,Halobacteriales;Halobacteriaceae;Halococcus",
		"Archaea;Euryarchaeota;Halobacteria,Halobacteriales;Halobacteriaceae;Halococcus",
		"Bacteria",
		"Bacteria",
		"Bacteria",
		...
	]
	"""
	# Use numpy ravel to extract list of tuples into a list of OTU descriptions
	otu_list = list(np.ravel(results))
	return jsonify(otu_list)

@app.route('/metadata/<sample>')
def sample_metadata(sample):
	"""Return the MetaData for a given sample."""
	sel = [Samples_Metadata.SAMPLE, Samples_Metadata.ETHNICITY,
		   Samples_Metadata.GENDER, Samples_Metadata.AGE,
		   Samples_Metadata.LOCATION, Samples_Metadata.BBTYPE]
	
	# sample[3:] strips the 'BB_'
	# the numeric value of 'SAMPLE'
	results = session.query(*sel).\
		filter(Samples_Metadata.SAMPLEID == sample[3:]).all()

	# Create a dictionary entry for each row of metadata information
	sample_metadata = {}
	for result in results:
		sample_metadata['SAMPLEID'] = result[0]
		sample_metadata['ETHNICITY'] = result[1]
		sample_metadata['GENDER'] = result[2]
		sample_metadata['AGE'] = result[3]
		sample_metadata['LOCATION'] = result[4]
		sample_metadata['BBTYPE'] = result[5]

	return jsonify(metadict)

@app.route('/wfreq/<sample>')
def sample_wfreq(sample):
	"""Return the Weekly Washing Frequency as a number."""

	#'sample[3:]'strips the 'BB_ ' prefix
	results = session.query(Samples_Metadata.WFREQ).\
		filter(Samples_Metadata.SAMPLEID == sample[3:]).all()
	wfreq = np.ravel(results)

	#Return only the first integer value for washing frequency
	return jsonify(int(wfreq[0]))

@app.route('/samples/<sample>')
def samples(sample):
	"""OTU IDs and Sample Values for a given sample.

	Sort your Pandas Dataframe (OTU ID and Sample Value)
	in Descending Order by Sample Value

	Return a list of dictionaries containing sorted lists for 'otu_ids'
	and 'sample_values'
	
	[
		{
			otu_ids: [
				1166,
				2858,
				481,
				...
			],
			sample_values: [
				163,
				126,
				113,
				...
			]
		}
	]
	"""
	stmt = session.query(Samples).statement
	df = pd.read_sql_query(stmt, session.bind)

	# Make sure that the sample
	if sample not in df.columns:
		return jsonify(f"Error! Sample: {sample} Not Found!"), 400	
	
	# Return any sample values
	df = df[df[sample] > 1]
	
	# Sort the results by samples
	df.sort_values(by=sample, ascending=0)
	
	# Format the data to send as JSON
	data = [{
		"otu_ids": df[sample].index.values.tolist(),
		"sample_values": df[sample].values.tolist()
	}]
	return jsonify(data)

###########################################################
# Default App Settings 
###########################################################
if __name__ == "__main__":
	app.run(debug=True)
=======
#Dependencies
from flask import Flask,jsonify

import datetime as datetime
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

####################################################################
# Database Setup
####################################################################

# Create Engine
engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Biodiversity = Base.classes.biodiversity

# Create our session (link) from Python to the DB
session = Session(engine)

#####################################################################
# Flask Setup
#####################################################################

app = Flask(__name__)

#####################################################################
# Flask Routes
#####################################################################


@app.route('/')
def dashboard():
    """Return the dashboard homepage"""
    return(index.html)(
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )

@app.route('/names')
def samplenames():
    """Returns a list of sample names in the format"""
    # Query all Belly Button Biodiversity
    results = session.query(Biodiversity.name).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    # print(all_names)
    return jsonify(all_names)

@app.route('/otu')
def otudescriptions():
    """Returns a list of OTU descriptions in the following format"""
    
    # Query all passengers
    results = session.query(Biodiversity).all()

    #Create a dictionary from the row data and append to a list 
    all_passengers = []
    for passengers in results:
        passengers_dict = {}
        passengers_dict["name"] = passengers.name
        passengers_dict["age"] = passengers.age
        passengers_dict["sex"] = passengers.sex
        all_passengers.append(passengers_dict)
    return jsonify(all_passengers)

@app.route('/metadata/<sample>')
def jsonify():
    results = session.query(Passengers).filter(Passenger.survived == 1)
    """Returns a json dictionary of sample metadata in the format"""
    
    survived_passengers = []
    for passengers in results:
        # if (passenger.survived ==1):
        passenger_dict = {}
        passenger_dict["name"] = passenger.name
        survived_passengers.append(passenger_dict)
    return jsonify(survived_passengers)

@app.route('/wfreq/<sample>')
def WFREQ():
    """Returns an integer value for the weekly washing frequency `WFREQ`"""
    return jsonify()

@app.route('/sample/<sample>')
def dictionaries():
    """Return a list of dictionaries containing sorted lists  for `otu_ids`
    and `sample_values`""" 
    return jsonify()

@app.route()
def dictionaries2():
    """Return a list of dictionaries containing sorted list for 'sample_values'"""
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> b6c85d893015c7e8d371a77ee99a34a0e91e4d45
