FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    build-essential

RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu124
RUN pip3 install 'git+https://github.com/huggingface/transformers.git'
RUN pip3 install accelerate
RUN pip3 install -i https://pypi.org/simple/ bitsandbytes
RUN pip3 install jupyter
RUN pip3 install gradio

WORKDIR /app

COPY . /app

#CMD ["python3", "app.py"]
