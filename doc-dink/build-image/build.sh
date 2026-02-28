# dinkydocker/dinky-standalone-server:1.2.5-flink1.20-dev
export DOCKER_TAG=dinkydocker/dinky-standalone-server
export DOCKER_VERSION=1.2.5-flink1.20-dev
docker rmi app/$DOCKER_TAG:$DOCKER_VERSION
docker build  --no-cache -t app/$DOCKER_TAG:$DOCKER_VERSION .
