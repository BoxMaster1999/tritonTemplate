from fastapi import status
from fastapi.routing import APIRouter

import numpy as np
import tritonclient.http.aio as httpclient
from tritonclient.utils import *

from .model import InputModel, OutputModel

textgen_router = APIRouter(prefix="/textgen")

URL = "triton-server:8000"


@textgen_router.post('/generate_v1',
             description='Inference textgen',
             tags=['Inference endpoints'],
             status_code=status.HTTP_200_OK,
             response_model=OutputModel)
async def generate_request(input_: InputModel) -> OutputModel:
    async with httpclient.InferenceServerClient(URL) as client:
        input_data = np.array([[input_.text]], dtype=np.object_)
        inputs = [
            httpclient.InferInput(
                "INPUT", input_data.shape, np_to_triton_dtype(np.object_)
            ),
        ]
        inputs[0].set_data_from_numpy(input_data)
        outputs = [
            httpclient.InferRequestedOutput("OUTPUT"),
        ]
        response = await client.infer('t5', inputs, outputs=outputs)
        output_data = response.as_numpy("OUTPUT").tolist()
    return OutputModel(output_object=output_data)
