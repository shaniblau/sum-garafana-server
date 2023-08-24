import logging as log
from fastapi import FastAPI

app = FastAPI()

log_format = '%(asctime)s ,%(message)s'
log.basicConfig(filename='alerts.log', format=log_format)
logger = log.getLogger('app_logger')


@app.post('/webhook')
async def get_webhook(alert: dict):
    logger.info(f'Alert received: {alert}')
    print(alert)
    return {"status": "success"}
