# 基于的基础镜像
FROM os/ubuntu:22.04
USER root
#
RUN mkdir -p /opt/tmp
# flink 添加到根目录
COPY jdk-21.0.7/ /opt/jdk
COPY flink-1.20.3/ /opt/flink
COPY docker-entrypoint.sh /docker-entrypoint.sh

# 设置环境变量
ENV JAVA_HOME=/opt/jdk
ENV CLASSPATH=$JAVA_HOME/lib:$CLASSPATH
ENV FLINK_HOME=/opt/flink
ENV PATH=$JAVA_HOME/bin:$FLINK_HOME/bin:$PATH
#ENV AWS_ACCESS_KEY=bgd
#ENV AWS_SECRET_KEY=xxxx
#ENV AWS_ENDPOINT=http://xxx.xxx.xxx.xxx:18820
ENV JAVA_OPTS="--add-opens java.base/java.util=ALL-UNNAMED"
#
# 设置code文件夹的工作目录
WORKDIR /opt/tmp

ENTRYPOINT ["/bin/bash","/docker-entrypoint.sh"]

EXPOSE 8081 8082
EXPOSE 6121 6122 6123 6124 6125
