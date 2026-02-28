FROM dinkydocker/dinky-standalone-server:1.2.5-flink1.20
#USER root

#
COPY flink-connector-jdbc-3.3.0-1.20.jar /opt/flink/lib/
COPY flink-doris-connector-1.20-24.0.1.jar /opt/flink/lib/
COPY flink-s3-fs-presto-1.20.3.jar /opt/flink/lib/
COPY flink-shaded-hadoop-3-uber-3.1.1.7.2.9.0-173-9.0.jar /opt/flink/lib/
COPY flink-shaded-zookeeper-3-3.8.3-19.0.jar  /opt/flink/lib/
COPY flink-sql-connector-kafka-3.3.0-1.20.jar /opt/flink/lib/
COPY kafka-clients-3.3.1.jar /opt/flink/lib/
COPY mysql-connector-java-8.0.27.jar  /opt/flink/lib/
#
RUN chmod +x /opt/flink/lib/*
#
RUN ln -s /opt/flink/lib/flink-connector-jdbc-3.3.0-1.20.jar /opt/dinky/extends/flink1.20/flink-connector-jdbc-3.3.0-1.20.jar
RUN ln -s /opt/flink/lib/flink-doris-connector-1.20-24.0.1.jar /opt/dinky/extends/flink1.20/flink-doris-connector-1.20-24.0.1.jar
RUN ln -s /opt/flink/lib/flink-s3-fs-presto-1.20.3.jar /opt/dinky/extends/flink1.20/flink-s3-fs-presto-1.20.3.jar
RUN ln -s /opt/flink/lib/flink-shaded-hadoop-3-uber-3.1.1.7.2.9.0-173-9.0.jar /opt/dinky/extends/flink1.20/flink-shaded-hadoop-3-uber-3.1.1.7.2.9.0-173-9.0.jar
RUN ln -s /opt/flink/lib/flink-shaded-zookeeper-3-3.8.3-19.0.jar /opt/dinky/extends/flink1.20/flink-shaded-zookeeper-3-3.8.3-19.0.jar
RUN ln -s /opt/flink/lib/flink-sql-connector-kafka-3.3.0-1.20.jar /opt/dinky/extends/flink1.20/flink-sql-connector-kafka-3.3.0-1.20.jar
RUN ln -s /opt/flink/lib/kafka-clients-3.3.1.jar /opt/dinky/extends/flink1.20/kafka-clients-3.3.1.jar
RUN ln -s /opt/flink/lib/mysql-connector-java-8.0.27.jar /opt/dinky/extends/flink1.20/mysql-connector-java-8.0.27.jar
