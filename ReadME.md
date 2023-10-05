## Few steps test run
Run docker with pre-build triton server (cuda 11.6 required):

    # HTTP Service: 8005:8000, GRPC Service: 8006:8001, Metric Service: 8007:8002, Jupyterlab: 8010:8888
    docker run --shm-size=1g -it --ulimit memlock=-1 -p 8005:8000 -p 8006:8001 -p 8007:8002 -p 8010:8888 --ulimit stack=67108864 nvcr.io/nvidia/tritonserver:22.02-py3 bash

Inside container run jupyter interface:

    pip install jupyterlab
    jupyter-lab --allow-root --port=8888 --no-browser --ip=0.0.0.0

Attach to jupyter and install torch for cuda 11.6:

    pip install torch --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu116
    

Run example of nvidia repo, make model folder with config:

    git clone https://github.com/triton-inference-server/python_backend -b r22.02
    cd python_backend
    mkdir -p models/add_sub/1/
    cp examples/add_sub/model.py models/add_sub/1/model.py
    cp examples/add_sub/config.pbtxt models/add_sub/config.pbtxt

Run inference server:

    tritonserver --model-repository `pwd`/models --log-verbose 3
