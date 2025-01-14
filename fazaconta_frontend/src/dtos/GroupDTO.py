from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from .FileData import FileData
from .UserDTO import UserDTO
from .MemberDTO import MemberDTO
from .PendingPaymentDTO import PendingPaymentDTO


class GroupDTO(BaseModel):
    id: UUID
    title: str
    created_by: UserDTO
    total_expense: float
    created_at: datetime
    members: list[MemberDTO]
    pending_payments: list[PendingPaymentDTO]
    image: FileData | None = None
