import os
from pathlib import Path
from configparser import ConfigParser


BASE_DIR = Path(__file__).parent

ROOT_DIR = BASE_DIR.parent

DATA_DIR = ROOT_DIR.joinpath(
    'data', 'satelit'
)
CHECK_PICTURE = ROOT_DIR.joinpath(
    "data", "check_picture", "t_cross", "picture.PNG"
)
MAP_DIR = ROOT_DIR.joinpath(
    'data', 'map'
)
DEVICE_FOLDER = ROOT_DIR.joinpath(
    'py_solution', 'devices'
)
CRED_FOLDER = ROOT_DIR.joinpath(
    'py_solution', 'cred'
)
MODELS_DIR = BASE_DIR.joinpath("models")

BATCH_SIZE = 32
IMG_HEIGHT = 180
IMG_WIDTH = 180
EPOCHS = 30

config = ConfigParser()
config.read(CRED_FOLDER.joinpath('tuya_cred.ini'))
# Select an endpoint base on your project availability zone	
# For more info, refer to: https://developer.tuya.com/en/docs/iot/api-request?id=Ka4a8uuo1j4t4	
ENDPOINT = "https://openapi.tuyaeu.com"	

# Cloud project authorization info	
ACCESS_ID = config["cred"]["access_id"]	
ACCESS_KEY = config["cred"]["access_key"]	
	
	
# Project configuration	
USERNAME = config["cred"]["username"]
PASSWORD = config["cred"]["password"]	