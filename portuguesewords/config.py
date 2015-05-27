from portuguesewords import app
from portuguesewords.local_config import SQLALCHEMY_DATABASE_URI

app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
