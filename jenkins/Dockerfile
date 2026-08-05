FROM jenkins/jenkins:lts

USER root

# Docker + Python + outils
RUN apt-get update && \
    apt-get install -y \
        docker.io \
        python3 \
        python3-pip \
        python3-venv \
        curl && \
    rm -rf /var/lib/apt/lists/*

# Installation du plugin Docker Compose
RUN mkdir -p /usr/libexec/docker/cli-plugins && \
    curl -SL https://github.com/docker/compose/releases/download/v2.39.2/docker-compose-linux-x86_64 \
    -o /usr/libexec/docker/cli-plugins/docker-compose && \
    chmod +x /usr/libexec/docker/cli-plugins/docker-compose

USER jenkins
