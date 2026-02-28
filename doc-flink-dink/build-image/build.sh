# app/flink-1.20.0:20250707
export BUILD_HOME=/home/bgd/bgd-data/flink/flink-1.20.3-k3s-dinky-1.2.5/build-images
export DOCKER_TAG=flink-1.20.3
export DOCKER_VERSION=20251218
docker rmi app/$DOCKER_TAG:$DOCKER_VERSION
docker build  --no-cache -t app/$DOCKER_TAG:$DOCKER_VERSION .
#cd $BUILD_HOME/build-images/sync
#bash sync.sh
