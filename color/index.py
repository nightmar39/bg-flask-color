from flask import Flask, render_template
import os

app = Flask(__name__)

version = os.getenv('COLOR')

mymap = {
	"RED" : "red.html",
	"GREEN" : "green.html",
	"BLUE" : "blue.html",
	"ORANGE" : "orange.html",
}

@app.route("/")
def show_version():
	return render_template(mymap[version])

@app.route("/test")
def test_route():
	response = {
		"version" : version
	}
	return response


if __name__ == "__main__":
    app.run()
