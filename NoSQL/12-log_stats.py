#!/usr/bin/env python3
"""
12-log_stats
Script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def main():
    """
    Script that provides some stats about Nginx logs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents({
        "method": "GET", "path": "/status"
        })
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
