docker rmi spark:3.5.5-pyspark-1.1
#docker build --no-cache -t spark:3.5.5-pyspark .
docker build --memory=6g -t spark:3.5.5-pyspark-1.1 .
