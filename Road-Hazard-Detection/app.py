import os
import shutil
from flask import Flask, render_template, request

app = Flask(__name__)

BASE = os.path.dirname(os.path.abspath(__file__))
UPLOAD = os.path.join(BASE, "static", "uploads")
RESULT = os.path.join(BASE, "static", "results")

os.makedirs(UPLOAD, exist_ok=True)
os.makedirs(RESULT, exist_ok=True)


@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":

        print("POST received")  # DEBUG

        if "file" not in request.files:
            return "No file key found"

        file = request.files["file"]

        if file.filename == "":
            return "No file selected"

        upload_path = os.path.join(UPLOAD, file.filename)
        result_path = os.path.join(RESULT, file.filename)

        file.save(upload_path)
        shutil.copy(upload_path, result_path)

        print("Saved to:", result_path)

        return render_template("index.html",
                            output_img="results/" + file.filename)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


