import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/exceptions.py",
    "src/logger.py",
    "src/utils.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipelines/__init__.py",
    "src/pipelines/train_pipeline.py",
    "src/pipelines/predict_pipeline.py",
    "Requirements.txt",
    "setup.py"
]

for filepath in list_of_files: 
    filepath = Path (filepath) 
    filedir, filename = os.path.split(filepath) 
    
    if filedir !="": 
        os.makedirs (filedir, exist_ok=True) 
        logging.info (f"Creating directory; {filedir} for the file: {filename}")
        
    if (not os.path.exists (filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f: 
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")