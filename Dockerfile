# Pull base image
FROM python:3.10.4-slim-bullseye
#FROM python:3.8.3-slim-buster
#hoping bin bash is installed
#FROM python:alpine:3.16

#create non-root user
ARG USERNAME=rick
ARG USER_UID=1000
ARG USER_GID=1000

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER $USERNAME

# Set work directory
WORKDIR /home/rick/code

# Install dependencies
COPY ./requirements.txt .
# uncomment this on a raspberry pi
#RUN apt-get update \
#    && apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt


# Copy project
COPY . .