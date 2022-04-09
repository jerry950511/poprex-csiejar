from flask import Flask, render_template, request, json, jsonify
import eportal
app = Flask(__name__)



@app.route('/')
def index_page():
  return render_template("index.html")


#run server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
