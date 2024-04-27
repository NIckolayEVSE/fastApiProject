from pydantic import BaseModel


class UsersData(BaseModel):
    phone: str
    address: str
