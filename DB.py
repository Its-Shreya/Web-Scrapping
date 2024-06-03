
from config.plagReportDB import client
from bson import ObjectId
import datetime as dt

from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.environ.get("DB_NAME")

db = client[DB_NAME]
collection = db["plagresults"]


def create_database(userId, submittedText, fileName, scanType, key):
    #print(submittedText)
    # fileName = submittedText.split(
    #     " ")[0] + " " + submittedText.split(" ")[1] + " " + submittedText.split(" ")[2]
    # print(fileName)
    createdAt = dt.datetime.utcnow()
    #print(createdAt)

    try:
        if key == "":
            result = collection.insert_one(
                {
                    "user": ObjectId(userId),
                    "submittedText": submittedText,
                    "results": [],
                    "status": "running",
                    "totalWords": 0,
                    "similarTexts": [],
                    "fileName": fileName,
                    "similarityPercent": "",
                    "createdAt": createdAt,
                    "scanType": scanType,
                    #                    "apiUser": ObjectId(key),
                }
            )
        elif key != "":
            result = collection.insert_one(
                {
                    #                   "user": ObjectId(userId),
                    "submittedText": submittedText,
                    "results": [],
                    "status": "running",
                    "totalWords": 0,
                    "similarTexts": [],
                    "fileName": fileName,
                    "similarityPercent": "",
                    "createdAt": createdAt,
                    "scanType": scanType,
                    "apiUser": ObjectId(key),
                }
            )
        res = collection.find_one({"_id": result.inserted_id})
        return dict(res)

    except Exception:
        print("--------------ERROR WHILE CREATING: Cannot insert in db----------------")
        pass


def update_database_result(id, results):
    try:
        collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": {"results": results}}
        )
        print("------------------Inserted to DB------------------")
    except Exception:
        print(
            "--------------ERROR WHILE UPDATING RESULTS: Cannot update in db----------------"
        )
        pass


def update_database_complete(id, wordCount, similarTexts, score, timeTaken):
    try:
        collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "totalWords": wordCount,
                    "similarTexts": list(similarTexts),
                    "status": "completed",
                    "similarityPercent": score,
                    "timeTaken": round(timeTaken, 2),
                }
            },
        )
        print("------------------Inserted to DB Complete------------------")

    except Exception:
        print(
            "--------------ERROR WHILE UPDATING COMPLETED: Cannot update in db----------------"
        )
        pass
