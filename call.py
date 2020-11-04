from flask import Flask, render_template, request, redirect
import logging
import os
from flask_cors import CORS
import demjson

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

app = Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)


@app.route('/', methods=["POST"])
def my():
	# caller = demjson.decode(request.args.get('caller'))
	caller = request.form['caller']
	receiver = request.form['receiver']
	# TODO: authenticate both numbers and return the callers

	return "response from Flask"




if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 4000)))
