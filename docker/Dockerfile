FROM ubuntu:22.04

ARG PYTHON_VERSION=3.10

WORKDIR /root

# Install basic packages
RUN apt-get update && apt-get install -y \
    vim \
    curl wget \
    zip unzip \
    git git-lfs

# Install Python
RUN apt-get update && apt-get install -y \
    python${PYTHON_VERSION} python${PYTHON_VERSION}-distutils python${PYTHON_VERSION}-dev \
    python-is-python3

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3.10 -
ENV PATH=$PATH:/root/.local/bin

# Cleanup
RUN apt-get autoremove -y && apt-get clean && \
    rm -rf /usr/local/src/* && rm -rf ~/.cache/pip && poetry cache clear pypi --all

# Command
WORKDIR /workspaces
CMD ["/bin/bash"]