from flask import Flask

app = Flask(__name__)

@app.route("/testing",methods=['GET'])
def home():
    return "Hello, AWS! welcome git  demo llama adam  "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
