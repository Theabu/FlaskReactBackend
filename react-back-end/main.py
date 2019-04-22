import flask 

app = flask.Flask("__main__")


@app.route('/')
def hello():

	return flask.render_template("index.html",token="hello its working fine")

app.run(debug='true')