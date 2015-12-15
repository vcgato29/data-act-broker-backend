import sys
import os

from flask import Flask, request, make_response, session, g, redirect, url_for, \
     abort, render_template, flash ,session, Response
import json
import flask

from handlers.aws.session import DynamoInterface, SessionTable, LoginSession
from handlers.loginHandler import LoginHandler
from handlers.fileHandler import FileHandler
from handlers.jobHandler import JobHandler
from fileRoutes import add_file_routes
from loginRoutes import add_login_routes

# Set parameters
debugFlag = True  # Should be false for prod
runLocal = True  # False for prod
createTable = False  # Should be false for most runs, true for first run with DynamoDB

# Get the project's root folder
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Create application
app = Flask(__name__)
app.config.from_object(__name__)

#Enable AWS Sessions
app.session_interface = DynamoInterface()


# Root will point to index.html
@app.route("/", methods=["GET"])
def root():
    filePath = os.path.join(PROJECT_ROOT, '..', 'index.html')
    content = open(filePath).read()
    return Response(content, mimetype="text/html")

# Create handler objects
jobManager = JobHandler()
fileManager = FileHandler(jobManager)
loginManager = LoginHandler()

# Add routes for modules here
add_login_routes(app, loginManager)
add_file_routes(app, fileManager)

if __name__ == '__main__':
    SessionTable.setup(app, runLocal, createTable)
    app.run(debug=debugFlag)
