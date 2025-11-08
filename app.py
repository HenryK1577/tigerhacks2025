from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import config
import my_secrets

app = Flask(__name__)

#Loading secrets (keys) into app config
app.config["MONGO_URI"] = my_secrets.MONGO_URI

bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template('base.html')