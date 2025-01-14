from uuid import UUID
from pydantic import BaseModel, Field
from .UserDTO import UserDTO


class MemberDTO(BaseModel):
    id: UUID
    user: UserDTO
    balance: float = Field(default=0.0)