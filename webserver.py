from flask import Flask
app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def hello_world():
  return """
    <h1 style='color: red;'>The bot is up and running...</h1>
    <code>Flask is <em>awesome</em></code>
    """
if __name__ == '__main__':
  app.run(host='0.0.0.0')