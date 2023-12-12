# write code which responsible to build entire project structure.not necessory file name should be template
# is me hum apny hesab se folder structure banay ge

import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "MLsetupProject"

'''
as we know in ML Structure we have component, in component have .. dataSource->data ingestion->data
transformation-> model training -> model monitering/evaluation, & pipeline have training pipeline and testing pipeline

'''
list_of_file = [
# as in github ... 1st make github folder 2nd while in deployment case we write code in gitgub action in workflow
# .gitkeep just show we make folder in future as we know as this time we do practice

    # ".github/workflows/.gitkeep",
    f"SourceFolder/{project_name}/__init__.py", # that __init__.py will make package in this folder location
    f"SourceFolder/{project_name}/components/__init__.py",
    f"SourceFolder/{project_name}/components/data_ingestion.py",
    f"SourceFolder/{project_name}/components/data_transformation.py",
    f"SourceFolder/{project_name}/components/model_training.py",
    f"SourceFolder/{project_name}/components/model_monitering.py",
    f"SourceFolder/{project_name}/pipelines/__init__.py",
    f"SourceFolder/{project_name}/pipelines/training_pipeline.py",
    f"SourceFolder/{project_name}/pipelines/prediction_pipeline.py",
    # and in also need some file in MLsetup project like 
    f"SourceFolder/{project_name}/exception_handling.py",
    f"SourceFolder/{project_name}/logger.py",
    f"SourceFolder/{project_name}/utils.py",
    "app.py",
    "dockerFile",
    "requirements.txt",
    "setup.py",
    
]


for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                logging.info(f"Creating empty file:{filepath}")

        else:
            logging.info(f"{filename} is already exist")
