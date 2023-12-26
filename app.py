from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/about")
def about_me():
  return "This is about me"
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)