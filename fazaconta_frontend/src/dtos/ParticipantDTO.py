from uuid import UUID
from pydantic import BaseModel
from .UserDTO import UserDTO


class ParticipantDTO(BaseModel):
    id: UUID
    user: UserDTO
    amount: float
