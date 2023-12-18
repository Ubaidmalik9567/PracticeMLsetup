import os
import sys 
from SourceFolder.MLsetupProject.exception_handling import CustomException
from SourceFolder.MLsetupProject.logger import logging
from SourceFolder.MLsetupProject.utils import get_sql_data
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts",'train.csv')
    test_data_path:str = os.path.join("artifacts",'test.csv')
    raw_data_path:str = os.path.join("artifacts",'raw_data.csv')

    '''
    # if we not use  dataclasses library then use this code

    class DataIngestionConfig:
    def __init__(self, train_data_path=None, test_data_path=None, raw_data_path=None):
        if train_data_path is None:
            train_data_path = os.path.join("artifacts", 'train.csv')
        if test_data_path is None:
            test_data_path = os.path.join("artifacts", 'test.csv')
        if raw_data_path is None:
            raw_data_path = os.path.join("artifacts", 'raw_data.csv')

        self.train_data_path = train_data_path
        self.test_data_path = test_data_path
        self.raw_data_path = raw_data_path
    
    '''

class DataIngestionsetup:
    def __init__(self) -> None:
        self.ingestionConfig = DataIngestionConfig()
    
    def initiation_DataIngestionConfig(self):

        try:
            # make new dir
            os.makedirs(os.path.dirname(self.ingestionConfig.raw_data_path),exist_ok=True)
            logging.info("Reading from phpMyAdmin") 
            dataset = get_sql_data()
            dataset.to_csv(self.ingestionConfig.raw_data_path, index=False, header=True)
            train_data,test_data = train_test_split(dataset,test_size=0.2,random_state=42) 
            train_data.to_csv(self.ingestionConfig.train_data_path, index=False, header=True)
            test_data.to_csv(self.ingestionConfig.test_data_path, index=False, header=True)
            logging.info("Data ingestion completed")

            return (
                self.ingestionConfig.train_data_path,
                self.ingestionConfig.train_data_path
                )



        except Exception as e:
            raise CustomException(e,sys)



