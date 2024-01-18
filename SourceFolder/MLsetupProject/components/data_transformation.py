# aim of data_transformation file is to get train_test_split data, perform feature
# engineering and get pickle file

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from SourceFolder.MLsetupProject.logger import logging
from SourceFolder.MLsetupProject.utils import save_file


import pickle
import os
import sys 
from dataclasses import dataclass
from SourceFolder.MLsetupProject.logger import logging
from SourceFolder.MLsetupProject.exception_handling import CustomException


@dataclass
class DataTransformation_filePath:
    pickle_filePath = os.path.join('artifacts','preprocessorFile.pkl')


class DataTransformation:
    def __init__(self):
        self.dataTransformation_config = DataTransformation_filePath() #store path in this variable

    def FeatureEngineeringSetup(self):
        # this function do Feature Transformation / dataTransformation
        try:
                        
            int_col = ['total_bill_', 'size_']
            cat_col = ['sex_', 'smoker_', 'day_', 'time_']

            numerical_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='mean'))
                ])
            
            
            categorical_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ohn',OneHotEncoder()),
                ])
            
            logging.info(f'numarical columns: {int_col}')
            logging.info(f'categorical columns: {cat_col}')

            # now combin both
            preprocessing = ColumnTransformer(transformers=[
                ('numerical_preprocessing',numerical_pipeline,int_col),
                ('categorical_preprocessing',categorical_pipeline,cat_col)
                ],remainder='passthrough'
                # can use 2nd method
            )

            return preprocessing
       
        except Exception as e:
            raise CustomException(e, sys)
        
         

     # initiate dataTransformation
    def initiate_featureEngineering(self,train_data_path,test_data_path):
        # train or test data_path is output of data_ingestion
        train_df = pd.read_csv(train_data_path, )
        test_df = pd.read_csv(test_data_path)
        print(train_df.head(4))

        logging.info('Reading train and test file')
        preprocessing_object = self.FeatureEngineeringSetup()

        # seprate x or y feature in both
        
       
        xFeature_trainData = train_df.drop(columns=['tip_'],axis=1)
        yFeature_trainData = train_df['tip_']
        
        xFeature_testData = test_df.drop(columns=['tip_'],axis=1)
        yFeature_testData = test_df['tip_']

        numerical_columns = ['total_bill_','size_']
        for column in numerical_columns:
                try:
                    xFeature_trainData[column] = xFeature_trainData[column].astype(int)
                    xFeature_testData[column] = xFeature_testData[column].astype(int)
                except ValueError:
                    # Handle non-integer values, e.g., convert them to NaN
                    xFeature_trainData[column] = pd.to_numeric(xFeature_trainData[column], errors='coerce')
                    xFeature_testData[column] = pd.to_numeric(xFeature_testData[column], errors='coerce')

            
        logging.info("Apply preprocessing techniques on train or test dataFrame")

        xdata = preprocessing_object.fit_transform(xFeature_trainData)
        ydata = preprocessing_object.transform(xFeature_testData)
        # both return preprocessing data in array formate

        # trainData_arr = np.concatenate(xdata,np.array(yFeature_trainData))
        # testData_arr = np.concatenate(ydata,np.array(yFeature_testData))
        
        trainData_arr = np.concatenate((xdata, np.array(yFeature_trainData).reshape(-1, 1)), axis=1)
        testData_arr = np.concatenate((ydata, np.array(yFeature_testData).reshape(-1, 1)), axis=1)


        logging.info("preprocessing fileData save ")
        

        # now we make common functionality function to save file in utils and use it
        save_file(
            file_path= self.dataTransformation_config.pickle_filePath,
            preprocessing_obj = preprocessing_object
            )
        

        return(
            trainData_arr,
            testData_arr,
            self.dataTransformation_config.pickle_filePath

        )









