from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
  return "SUCCESS (from authservicesweb::root)\n"

if __name__ == "__main__":
    app.run()
