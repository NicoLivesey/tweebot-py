import tweepy
import gpt_2_simple as gpt2

import tweebot_py.config as cfg
from tweebot_py.utils import log


sess = gpt2.start_tf_sess()

@log("Model loading")
def load_model(model_dir, model):
    gpt2.load_gpt2(sess, run_name=cfg.DEFAUT_MODEL, checkpoint_dir=cfg.MODEL_DIR)


def _split(text):
    return text.split(cfg.SEP_WORD)

@log("Tweets generating")
def generate():
    text = gpt2.generate(
        sess,
        run_name=cfg.DEFAUT_MODEL,
        checkpoint_dir=cfg.MODEL_DIR,
        return_as_list=True,
        length=2000,
        temperature=0.5,
    )[0]
    return _split(text)

@log("Tweets uploading")
def upload(tweets):
    auth = tweepy.OAuthHandler(cfg.CONSUMER_KEY, cfg.CONSUMER_SECRET)
    auth.set_access_token(cfg.ACCESS_TOKEN, cfg.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    for tweet in tweets:
        # upload tweet into draft
