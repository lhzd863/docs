FROM os/ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# 1. 安装 Python 和依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        python3-venv \
        python3-full \
        curl \
        gcc \
        g++ \
        make \
        libssl-dev \
        libffi-dev \
        ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 2. 安装 Poetry 2.x（使用官方脚本）
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml README.md ./

# 3. 配置 Poetry 在项目内创建虚拟环境
RUN poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true

# 4. 安装依赖
RUN poetry install --no-interaction

# 5. 激活项目虚拟环境
ENV PATH="/app/.venv/bin:$PATH"

# 6. 验证
RUN echo "✅ 构建成功！" && \
    echo "Python: $(python --version)" && \
    echo "Poetry: $(poetry --version)" && \
    echo "虚拟环境: $(which python)"
