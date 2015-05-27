from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)


import portuguesewords.config
db = SQLAlchemy(app)

import portuguesewords.models
import portuguesewords.views
