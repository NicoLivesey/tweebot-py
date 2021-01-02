from tweebot_py.service import load_model, _split, generate, upload


def test_load_model():
    assert load_model() == None


def test_split():
    assert _split("a<|endoftext|>a") == ["a", "a"]


def test_generate():
    load_model()
    assert type(generate()) == list


# def test_upload():

