FROM flink:1.20

#
COPY jdk-17.0.12/ /opt/jdk
COPY dinky-app-1.20-1.2.5-jar-with-dependencies.jar /opt/flink/lib/
COPY dinky-catalog-mysql-1.20-1.2.5.jar /opt/flink/lib/
COPY dinky-catalog-postgres-1.20-1.2.5.jar /opt/flink/lib/
COPY dinky-client-1.20-1.2.5.jar /opt/flink/lib/
COPY clickhouse-jdbc-0.3.2-patch11.jar  /opt/flink/lib/
COPY commons-cli-1.3.1.jar  /opt/flink/lib/
COPY flink-connector-jdbc-3.3.0-1.20.jar  /opt/flink/lib/
COPY flink-doris-connector-1.20-24.0.1.jar  /opt/flink/lib/
COPY flink-sql-avro-1.20.3.jar   /opt/flink/lib/
COPY flink-sql-avro-confluent-registry-1.20.3.jar  /opt/flink/lib/
COPY flink-sql-connector-elasticsearch7-3.0.0-1.16.jar  /opt/flink/lib/
COPY flink-sql-connector-kafka-3.3.0-1.20.jar  /opt/flink/lib/
COPY flink-sql-connector-mongodb-1.0.0-1.16.jar  /opt/flink/lib/
COPY flink-sql-orc-1.20.3.jar  /opt/flink/lib/
COPY flink-sql-connector-rabbitmq-3.0.0-1.16.jar  /opt/flink/lib/
COPY flink-sql-protobuf-1.20.3.jar  /opt/flink/lib/
COPY mssql-jdbc-12.10.1.jre8.jar  /opt/flink/lib/
COPY kafka-clients-3.3.1.jar  /opt/flink/lib/
COPY ojdbc8-23.7.0.25.01.jar  /opt/flink/lib/
COPY postgresql-42.7.6.jar  /opt/flink/lib/
COPY trino-jdbc-476.jar  /opt/flink/lib/
COPY mysql-connector-java-8.0.27.jar  /opt/flink/lib/
COPY mysql-connector-java-5.1.44.jar /opt/flink/lib/
COPY flink-table-planner_2.12-1.20.3.jar  /opt/flink/lib/
COPY neo4j-java-driver-5.28.9.jar /opt/flink/lib/
COPY neo4j_c2-0.0.1.jar /opt/flink/lib/
#
#RUN rm -f /opt/flink/lib/flink-table-planner-loader-1.20.3.jar

# Prepare environment
ENV JAVA_HOME=/opt/jdk
ENV CLASSPATH=$JAVA_HOME/lib:$CLASSPATH
#ENV FLINK_HOME=/opt/flink
ENV PATH=$FLINK_HOME/bin:$JAVA_HOME/bin:$PATH
ENV JAVA_OPTS="--add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED"
ENV FLINK_ENV_JAVA_OPTS="--add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED"
#RUN groupadd --system --gid=9999 flink && \
#    useradd --system --home-dir $FLINK_HOME --uid=9999 --gid=flink flink
#WORKDIR $FLINK_HOME

# Install Flink
#COPY flink-1.20.3/ /opt/flink
