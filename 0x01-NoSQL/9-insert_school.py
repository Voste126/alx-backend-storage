#!/usr/bin/env python3
"""
insert a document in python

"""
import pymongo

def insert_school(mongo_collection, **kwargs):
    """
    insert document into a collection

    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
