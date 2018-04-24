FROM node:latest

# Install bleno and dependencies ---------------
# bluetooth IS required despite we do service bluetooth stop in the end
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -yqq \
    build-essential \
    bluetooth \
    bluez \
    emacs \
    libbluetooth-dev \
    libudev-dev \
    usbutils \
    && rm -rf /var/lib/apt/lists/*		   

RUN npm install bleno 

WORKDIR /root

# Cleaning up and final setup -------------------------
RUN apt-get autoremove -yqq
RUN apt-get clean

RUN service bluetooth stop