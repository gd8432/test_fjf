import os

from flask import Flask

app = Flask(__name__)


@app.route("/",methods=['POST'])
def hello_world():
    """Example Hello World route."""
    name = request.form.get("NAME", "World")
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
