# Tweebot_py #

### Summary ###

This repository is a tool to create a Twitter bot based on all tweets from a specific user.
It handles all the following steps:
- Tweets extraction
- Language modeling
- API deployement
- Bot creation

The model behind is a small GPT-2 (124M) inspired by https://github.com/aquadzn/gpt2-french/
It uses the library https://github.com/minimaxir/gpt-2-simple based on Tensorflow

### Installation and setup ###

You can either use Makefile or directly install dependencies by hand

* Make:

Just run and you're good:

```shell
make init
```

* By hand:

Run:

```shell
pip install -r requirements/requirements_runtime.txt
```

* Docker:

This project is encapsulated in a docker container so you should have **Docker** installed on your environment. For more info check https://docs.docker.com/get-docker/

To build and run the container:

```shell
docker build -t tweebot:latest .
docker run --name tweebot --rm -p 80:80 -it tweebot
```

### Run tests ###

To run them just do:

```shell
make test
```

### Contact ###

Nicolas HENRY: nicolas.h@lajavaness.com