from uuid import UUID
from pydantic import BaseModel, Field, HttpUrl


class GetGroupByUserIdResponse(BaseModel):
    id: UUID
    title: str
    image_src: HttpUrl | str | None
