from pydantic import BaseModel


class Pix(BaseModel):
    type: str
    value: str
