# This is our configuration file to configure Flask to our app location & variables needed to run Flask

import os  # operating system 
from dotenv import load_dotenv  # allows us to load our environment variables (variables needed to run application)

# Establish our base directory so whenever we use "." to reference any location in our app it knows we are referencing
# rangers_shop folder 
basedir = os.path.abspath(os.path.dirname(__file__))

# Need to establish where our environment variables are coming from (this file will be hidden from GitHub)
load_dotenv(os.path.join(basedir, '.env'))

# Create our Config class 
class Config():

    """
    Create Config class which will setup our configuration variables.
    Using Environment variables where available other create config variables. 
    """

    FLASK_APP = os.environ.get('FLASK_APP')  # looking for key of FLASK_APP in our environment variable location (.env)
    FLASK_ENV = os.environ.get('FLASK_ENV') 
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or '__porsche__'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')  # rangers_shop folder
