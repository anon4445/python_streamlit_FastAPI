from fastapi import FastAPI
import time
import logging
from fastapi.logger import logger as fastapi_logger

# Initialize FastAPI app
app = FastAPI()

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = fastapi_logger

@app.get("/concurrency_test1")
def concurrency_test1(id: int):
    for i in range(10):
        # Log the message with the current id
        logger.info(f"[concurrency_test1] id={id}")
        # Pause the execution for 1 second
        time.sleep(1)
    # Return a simple JSON response
    return {'detail': 'OK'}
