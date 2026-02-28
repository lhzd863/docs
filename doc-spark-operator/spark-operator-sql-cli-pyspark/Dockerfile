# 使用官方Spark镜像作为基础
FROM spark:3.5.5

# 切换到root用户以执行安装操作
USER root

# 创建用于存放外部依赖JAR包的目录
RUN mkdir -p /opt/spark/jars/external
RUN mkdir -p /opt/plugin
RUN mkdir -p /opt/spark/jobs
# 将本地已下载的Hadoop AWS和AWS SDK Bundle等JAR包复制到镜像中
# 请确保这些JAR包与Dockerfile在同一目录或使用正确的路径
# S3支持依赖JAR
COPY hadoop-aws-3.3.4.jar /opt/spark/jars/external/
COPY aws-java-sdk-bundle-1.12.262.jar /opt/spark/jars/external/
# iceberg支持依赖的JAR
COPY iceberg-spark-runtime-3.5_2.12-1.10.0.jar /opt/spark/jars/external/
COPY iceberg-aws-bundle-1.10.0.jar /opt/spark/jars/external/
# graphframes
COPY graphframes-spark3_2.12-0.10.0.jar /opt/spark/jars/external/
COPY graphframes-graphx-spark3_2.12-0.10.0.jar /opt/spark/jars/external/
COPY graphframes-connect-spark3_2.12-0.10.0.jar /opt/spark/jars/external/
# jdbc
COPY mysql-connector-java-8.0.27.jar /opt/spark/jars/external/
COPY mysql-connector-java-5.1.44.jar /opt/spark/jars/external/
COPY postgresql-42.7.3.jar /opt/spark/jars/external/
# neo4j
COPY neo4j-spark-connector-5.3.9-s_2.12.jar /opt/spark/jars/external/

#
#COPY unitycatalog-spark_2.12-0.2.1.jar /opt/spark/jars/external/
#COPY unitycatalog-spark_2.13-0.3.0.jar /opt/spark/jars/external/
# 客户端提交sql语句
COPY spark-sql-cli-1.0.jar /opt/plugin/

# 确保JAR文件具有可读权限
RUN chmod 644 /opt/spark/jars/external/*.jar
RUN chmod 777 /opt/plugin/*.jar
RUN chmod 777 /opt/spark/jobs

RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list

# pyspark
# 更新软件源并安装基础依赖
RUN apt-get update && \
    apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev \
    libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev \
    cmake pkg-config \
    wget curl liblzma-dev libbz2-dev ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY Python-3.12.9.tar.xz /opt/tmp/
RUN cd /opt/tmp && \
    tar -xf Python-3.12.9.tar.xz && \
    cd Python-3.12.9 && \
    ./configure --enable-optimizations --with-ssl-default-suites=openssl --prefix=/usr/local/python3.12 --with-ensurepip=install && \
    make -j$(nproc) && \
    make install && \
    cd / && \
    rm -rf /opt/Python-3.12.9*

# 创建符号链接
RUN ln -sf /usr/local/python3.12/bin/python3.12 /usr/bin/python3 && \
    ln -sf /usr/local/python3.12/bin/pip3.12 /usr/bin/pip3

# 配置 pip 使用国内镜像源（HTTP，避免 SSL 问题）
RUN pip3 config set global.index-url http://pypi.tuna.tsinghua.edu.cn/simple/ && \
    pip3 config set install.trusted-host pypi.tuna.tsinghua.edu.cn

# 安装setuptools（包含distutils功能）
RUN pip3 install setuptools wheel

# 安装 Poetry
RUN pip3 install poetry
# 配置Poetry（使用模块方式确保可靠）
RUN python3 -m poetry config virtualenvs.create false

# 复制 pyproject.toml
COPY pyproject.toml ./

# 使用 Poetry 安装依赖（包括 PySpark）
RUN python3 -m  poetry install --only=main --no-interaction --no-root


WORKDIR /opt/spark/jobs

# 验证安装
RUN python3 -c "import pyspark; print('PySpark version:', pyspark.__version__)" && \
    python3 -c "import pandas; print('Pandas version:', pandas.__version__)" && \
    python3 -c "import numpy; print('NumPy version:', numpy.__version__)" && \
    echo "All packages installed successfully"

ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

CMD ["python3", "--version"]
