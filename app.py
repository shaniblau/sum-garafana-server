from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def get_webhook():
    print(request.json)
    return Response(status=200)