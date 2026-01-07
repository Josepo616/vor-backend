from pydantic import BaseModel, EmailStr, ConfigDict

# Base: shared fields
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    is_active: bool = True

# Create: the recived data when registering
class UserCreate(UserBase):
    password: str

# Response: what is returned (excluding sensitive info)
class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True) # before: orm_mode = True
