import os

PROJECT_NAME = "tweebot-py"
VERSION = "0.1"
PORT = os.getenv("PORT")
LOG_LEVEL = os.getenv("LOG_LEVEL")

DEFAULT_MODEL = "hugo-romans"
MODEL_DIR = "/models/models/checkpoint/hugo"
DATA_DIR = "/data"
SEP_WORD = "<|endoftext|>"

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
