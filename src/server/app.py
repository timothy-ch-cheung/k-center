from flask import Flask, render_template
import os
print(os.getcwd())

app = Flask("__main__", static_folder="../../webapp/build/static", template_folder="../../webapp/build")


@app.route("/")
def index():
    return render_template('index.html')


app.run(debug=True)
