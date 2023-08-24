from flask import Flask, Response, request
import logging as log

app = Flask(__name__)
log_format = '%(asctime)s ,%(message)s'
log.basicConfig(filename='alerts.log', format=log_format)
logger = log.getLogger('app_logger')


@app.route('/webhook', methods=['POST'])
def get_webhook():
    logger.info(f'alert received, reason: {request.json}')
    print(request.json)
    return Response(status=200)