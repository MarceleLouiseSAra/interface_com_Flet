from uuid import UUID
from pydantic import BaseModel, field_serializer
from .FileData import FileData
from .Pix import Pix


class UserDTO(BaseModel):
    id: UUID
    name: str
    nickname: str
    email: str
    phone_number: str
    profile_photo: FileData | None
    pix: Pix | None

    @field_serializer("id")
    def serialize_dt(self, id: UUID, _info):
        return str(id)
