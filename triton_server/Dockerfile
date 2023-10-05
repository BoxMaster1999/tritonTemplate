# Образ c torch для cuda 11.6
FROM nvcr.io/nvidia/tritonserver:22.02-py3 as base

RUN pip install --upgrade pip && \
    pip install torch --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu116 && \
    pip install jupyterlab

RUN mkdir -p /opt/tritonserver/model_repository

# Образ для разработки
FROM base as dev
CMD jupyter-lab --allow-root --port=8888 --no-browser --ip=0.0.0.0

# Образ для теста
FROM base as test
CMD tritonserver --model-repository /opt/tritonserver/model_repository --log-verbose 3
