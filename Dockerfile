FROM python:3.6

# Set up code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install Linux dependencies
RUN apt-get update && apt-get install -y libssl-dev libffi-dev autoconf automake libtool vim build-essential pkg-config libgmp-dev
RUN apt-get install -y libsecp256k1-dev

# Copy over requirements
COPY requirements.txt .
# Install python dependencies
RUN pip install -r requirements.txt

COPY pymaker ./pymaker/
COPY utils ./utils/
COPY Makefile ./Makefile/
COPY app.py ./app.py


