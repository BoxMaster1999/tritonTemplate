from pydantic import BaseModel


class InputModel(BaseModel):
    text: str

class OutputModel(BaseModel):
    output_object: list
