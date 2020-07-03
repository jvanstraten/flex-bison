#!/bin/sh

rm -rf dist

docker build --pull -t flex-bison-wheel . && \
docker run -it --name flex-bison-wheel flex-bison-wheel && \
docker cp flex-bison-wheel:/io/dist/ .

docker rm flex-bison-wheel
