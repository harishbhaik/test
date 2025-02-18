from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/testing",methods=['GET'])
def home():
    return "Hello, AWS! welcome git  demo llama adam  "


@app.route("/view",methods=['GET'])
def view():
    return "Hey this just test version to find the process"


@app.route("/home",methods=['GET'])
def about():
    return render_template("home.html")

@app.route("/main",methods=['GET'])

def main():
    return "new branch"


@app.route("/about",methods=['GET'])

def about_new():
    return "new app route"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
