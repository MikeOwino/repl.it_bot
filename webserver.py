from flask import Flask
app = Flask(__name__)


import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def hello_world():
  return """
    <h1 style='color: black;'>The bot is up and running...</h2>
    <img src="https://w.wallhaven.cc/full/4g/wallhaven-4g95z7.png" width="1500" height="700">
    """
if __name__ == '__main__':
  app.run(host='0.0.0.0')