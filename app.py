from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return("<h1> Welcome to your flask App </h1>")
	

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(port = port)