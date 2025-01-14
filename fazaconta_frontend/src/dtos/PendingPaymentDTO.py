from uuid import UUID
from pydantic import BaseModel, Field

from .UserDTO import UserDTO


class PendingPaymentDTO(BaseModel):
    id: UUID
    from_user: UserDTO
    to_user: UserDTO
    amount: float = Field(ge=0)
