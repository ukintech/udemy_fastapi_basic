from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime

class ContactList(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    created_at: datetime
    class Config:
        from_attriubte = True

class ContactBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    gender: int = Field(...,strict=True, ge=0, le=1)
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)
    class Config:
        from_attriubte = True

class ContactDetail(ContactBase):
    id: int
    created_at: datetime
    class Config:
        from_attriubte = True

class ContactCreate(ContactBase):
    pass


