import fire
import gpt_2_simple as gpt2
from pathlib import Path

from tweebot_py.log import log
from tweebot_py import config as cfg


@log("GPT2 Training")
def train(name):
    path = Path(cfg.DATA_DIR) / name
    sess = gpt2.start_tf_sess()
    gpt2.finetune(
        sess,
        dataset=path,
        model_name=cfg.PRETRAINED_MODEL,
        model_dir=cfg.MODEL_DIR,
        steps=cfg.STEPS,
        batch_size=cfg.BATCH_SIZE,
        restore_from="latest",  # change to 'latest' if restarting fine-tuning from saved checkpoint
        checkpoint_dir=cfg.MODEL_DIR,  # if wanting to save checkpoints
        run_name=f"{name}-{cfg.PRETRAINED_MODEL}",
        print_every=10,
        learning_rate=cfg.LEARNING_RATE,
        sample_every=50,
        sample_length=1024,
        sample_num=1,
        save_every=int(
            cfg.STEPS / 4
        ),  # if the fine-tuning is very slow, lower this number
        overwrite=True,
    )


@log("Model Loading")
def _load_model(name):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(
        sess,
        run_name=name,
        checkpoint_dir=cfg.MODEL_DIR,
    )
    return sess


@log("Fake Tweets generating")
def _generate(sess, name):
    return gpt2.generate(
        sess,
        run_name=name,
        checkpoint_dir=cfg.MODEL_DIR,
        return_as_list=True,
        length=2048,
        temperature=cfg.TEMPERATURE,
    )[0]


def generate(name):
    run_name = f"{name}-{cfg.PRETRAINED_MODEL}"
    sess = _load_model(run_name)
    text = _generate(sess, run_name)
    text = text.split("<|endoftext|>")
    for t in text:
        print(t)


if __name__ == "__main__":
    fire.Fire()