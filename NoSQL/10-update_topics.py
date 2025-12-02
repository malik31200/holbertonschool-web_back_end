#!/usr/bin/env python3
"""
Update all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school
    Args:
        mongo_collection: pymongo collection object
        name: string, school name to update
        topics: list of strings, topics to set
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
