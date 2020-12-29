# TWEEBOT_PY #

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

* For dev:

This project is encapsulated in a docker container so you should have **Docker** installed on your environment. For more info check https://docs.docker.com/get-docker/

To build and run the container:

```shell
docker build -t api-cv-ads-bbox:latest .
docker run --name api-cv-ads-bbox --rm -p 80:80 -it api-cv-ads-bbox
```

### Run tests ###

The unit tests are containerized within the app image. To run them just do:

```shell
docker build -f Dockerfile_tests -t api-cv-ads-bbox-tests:latest .
docker run -v /path/to/data/folder:/data --name api-cv-ads-bbox-tests --rm -it api-cv-ads-bbox-tests
```

### Contact ###

Nicolas HENRY: nicolas.h@lajavaness.com