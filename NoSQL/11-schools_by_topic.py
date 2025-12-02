#!/usr/bin/env python3
"""
Returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school:
        Args:
            mongo_collection: pymongo collection object
            topic: string, topic to search
    """
    result = mongo_collection.find({"topics": topic})
    return list(result)
