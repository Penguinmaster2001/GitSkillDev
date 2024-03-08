FROM ubuntu:20.04

LABEL author="Anthony Cieri"
LABEL email="penguinmillion@gmail.com"
LABEL description="ROS2 Dockerfile for UVEEC Git / Unix skilldev."

RUN apt-get update && apt-get install -y \
    vim \
    python3 \
    git \
    nano

RUN useradd --create-home --groups sudo --shell /bin/bash uveec
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER root
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER uveec
WORKDIR /home/uveec/

CMD ["bash"]
