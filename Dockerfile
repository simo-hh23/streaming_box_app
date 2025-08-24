# Use Ubuntu 24.04 LTS as base
FROM ubuntu:24.04

# Prevent prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and required packages
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-setuptools \
    python3-pyqt5 \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
WORKDIR /app
COPY . /app

# Install any Python packages you need (if not in base)
RUN pip3 install --no-cache-dir PyQt5

# Set default display (host's X11)
ENV DISPLAY=:0

# Run the app
CMD ["python3", "streaming_services_list.py"]
