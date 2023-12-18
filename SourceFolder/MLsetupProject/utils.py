# reading of sql data we write in utils.py
import os
import sys
from SourceFolder.MLsetupProject.logger import logging
from SourceFolder.MLsetupProject.exception_handling import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv() 
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
dbname = os.getenv("dbname")

def get_sql_data():
    logging.info("Reading start from database")

    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=dbname
        )

        logging.info("Connection Establish! %s", mydb)
        data = pd.read_sql_query("Select * from tips",mydb)
        print(data.head())
        
        return data 

    except Exception as e:
        raise CustomException(e)
    