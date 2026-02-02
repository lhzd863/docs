#
DEV_VERSION="20260127"
#
docker rmi rest-dev:$DEV_VERSION
#
docker build -t rest-dev:$DEV_VERSION -f ./Dockerfile .
#
