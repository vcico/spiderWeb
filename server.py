from flask import Flask
app = Flask(__name__)




@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/<path:url>")
def mirror(url):
	return "the url is %s" % url


if __name__ == "__main__":
	    app.run()
