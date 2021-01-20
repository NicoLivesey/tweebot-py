import os

PROJECT_NAME = "tweebot-py"
VERSION = "0.1"
PORT = int(os.getenv("PORT"))
LOG_LEVEL = os.getenv("LOG_LEVEL")

DATA_DIR = "data"
SEP_WORD = "<|endoftext|>"

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

PRETRAINED_MODEL = os.getenv("PRETRAINED_MODEL", "romans")
MODEL_DIR = "models/checkpoint"
STEPS = os.getenv("STEPS", 500)
BATCH_SIZE = os.getenv("BATCH_SIZE", 8)
