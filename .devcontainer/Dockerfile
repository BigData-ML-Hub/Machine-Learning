# Use official PyTorch image with CUDA 11.8
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Set working directory
WORKDIR /workspace

# Install basic utilities
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    zip \
    unzip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Oh My Bash
RUN git clone https://github.com/ohmybash/oh-my-bash.git ~/.oh-my-bash \
    && cp ~/.oh-my-bash/templates/bashrc.osh-template ~/.bashrc \
    && rm -rf ~/.oh-my-bash

# Install Python dependencies (make sure to create your requirements.txt)
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command
CMD [ "bash" ]
