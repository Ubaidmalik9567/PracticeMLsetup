from SourceFolder.MLsetupProject.logger import logging
from SourceFolder.MLsetupProject.exception_handling import CustomException
from SourceFolder.MLsetupProject.components.data_ingestion import DataIngestionConfig
from SourceFolder.MLsetupProject.components.data_ingestion import DataIngestionsetup
from SourceFolder.MLsetupProject.components.data_transformation import DataTransformation
import sys


if __name__ == "__main__": # execution file point
    logging.info("execution has been strated")


try:
    # Some code that may raise an exception
    # x = 1 / 0
    # config = DataIngestionConfig()
    data_ingestion = DataIngestionsetup()
    data_ingestion.initiation_DataIngestionConfig()
    train_data,test_data = data_ingestion.initiation_DataIngestionConfig()
    data_transformation = DataTransformation()
    data_transformation.initiate_featureEngineering(train_data,test_data)
    

except Exception as e:
    logging.info("Custom Exception")
    # Call the error_message_details function to get a detailed error message
    raise CustomException(e, sys)
    


