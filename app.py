from flask import Flask, request
import json, logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s, %(message)s')
# logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('InterfaceLogger')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    return {"user":"whiskeymikey"}

@app.route("/metrics")
def metrics():
    response = app.make_response(json.dumps({"data": {"UserCount": 140, "UserCountActive": 23}}))
    response.headers["X-Sup"] = "sup header"
    response.set_cookie("lol","lol")
    response.status_code = 200
    response.mimetype = "application/json"

    logger.debug(f'{request.path} endpoint was reached')  
    # logger.info(f'this is an info message')
    # logger.warning(f'this is a warning message')
    # logger.error(f'this is an error message')
    # logger.critical(f'this is a critical message')  
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
