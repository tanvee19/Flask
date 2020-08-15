from flask import Flask,render_template
app = Flask("pitho")
app.secret_key = "python"
app.debug = True
from pitho.controllers import *
