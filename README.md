# CommandRPlus4bitForDocker

## Description
CommandRPlus4bitForDocker is a Dockerized environment for running a machine learning model that utilizes a 4-bit optimized version of the CommandR model by CohereForAI. It is equipped with Jupyter Notebook and Gradio interfaces to facilitate interaction and experimentation. The model and tokenizer are pre-loaded and ready for use on a CUDA-enabled device.

## Features
- Docker integration with NVIDIA GPU support.
- Jupyter Notebook for interactive code manipulation.
- Gradio interface for easy model testing via a web UI.

## Prerequisites
- Docker installed on your machine.
- NVIDIA Docker if running on a machine with an NVIDIA GPU.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CommandRPlus4bitForDocker.git
   ```
2. Navigate to the directory:
   ```bash
   cd CommandRPlus4bitForDocker
   ```

## Build and Run Docker Container
To build and run the Docker container, execute:
```bash
docker-compose up --build
```

## Usage
Once the Docker container is up and running:
- Access Jupyter Notebook at `http://localhost:8888`.
- Interact with the Gradio interface at `http://localhost:7860`.

## Model Interaction
To generate responses via the Gradio interface:
- Enter the text for which you need a generated response.
- Submit the text, and the model will provide a generated output based on the provided input.

## License
This project is licensed under the MIT License.