import logging
import os
from datetime import datetime 

log_file = f"{datetime.now().strftime('%m-%d-%Y %I-%M-%S %p')}.log"  # Use hyphens and dashes instead of slashes
log_path = os.path.join(os.getcwd(), "logs")  # Remove the log_file from the path
os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
