# UOCIS322 - Project 6 #
Brevet time calculator with MongoDB, and a RESTful API!

Read about MongoEngine and Flask-RESTful before you start: [http://docs.mongoengine.org/](http://docs.mongoengine.org/), [https://flask-restful.readthedocs.io/en/latest/](https://flask-restful.readthedocs.io/en/latest/).

## Overview

For this project, `Brevets` is organized into two separate services:

* Web (Front-end)
	* Time calculator (basically everything you had in project 4)
* API (Back-end)
	* A RESTful service to expose/store structured data in MongoDB.

This application is used in order to calculate brevet opening and closing times for a ACP Brevet bicycle race. It does this through a Javascript-Flask interaction and then stores it using the Submit and Display buttons. For this project I have changed the database used from pymongo to a RESTful API framework.

## API Documentation

In order to implement the API I created a a couple of API models in models.py that represent all the values we need to store from the webpage. These models are then used by the resources I created in brevet.py and brevets.py called BrevetResource and BrevetsResource that are added to the mongodb via the flask_api.py file which connects to mongodb.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani. Completed by Kyle Pinkham
