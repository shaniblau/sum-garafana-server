from flask import Flask, Response
import logging as log

app = Flask(__name__)
log_format = '%(asctime)s ,%(message)s'
log.basicConfig(filename='alerts.log', format=log_format)
logger = log.getLogger('app_loger')


@app.route('/webhook', methods=['POST'])
def get_webhook(alert):
    logger.info(f'alert received, reason: {alert.json}')
    print(alert.json)
    return Response(status=200)
