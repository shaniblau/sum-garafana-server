import logging as log
from fastapi import FastAPI

app = FastAPI()

log_format = '%(asctime)s ,%(message)s'
log.basicConfig(filename='alerts.log', format=log_format)
logger = log.getLogger('app_logger')


@app.post('/webhook')
async def get_webhook(alert):
    logger.info(f'alert received, reason: {alert.json()}')
    print(alert.json())
    return {"status": "success"}
