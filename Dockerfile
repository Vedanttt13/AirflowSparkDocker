FROM apache/airflow:2.7.1-python3.11

USER root

# Install Java and other dependencies
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-11-jdk procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME for Windows Docker (usually amd64)
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
RUN export JAVA_HOME

USER airflow

# Install Python packages
RUN pip install --no-cache-dir \
    apache-airflow-providers-apache-spark==4.0.0 \
    pyspark==3.4.1
