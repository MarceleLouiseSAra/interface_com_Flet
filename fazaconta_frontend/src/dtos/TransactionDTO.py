from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from .GroupDTO import GroupDTO
from .ParticipantDTO import ParticipantDTO
from .UserDTO import UserDTO


class TransactionDTO(BaseModel):
    id: UUID
    group: GroupDTO
    title: str
    amount: float
    paid_by: UserDTO
    transaction_type: str
    created_at: datetime
    participants: list[ParticipantDTO]
