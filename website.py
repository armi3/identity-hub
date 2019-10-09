import os
import yaml
from flask import Flask, render_template

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Fer González")
environment = os.getenv("ENVIRONMENT", "development")

with open('info.yml') as f:
    info = yaml.load(f, Loader=yaml.FullLoader)

print(info)
print(info['identities']['github'])

@app.route("/")
def profile():
    return render_template("hub.html", info=info)


if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    print("Local change.")
    app.run(host="0.0.0.0", debug=debug)
