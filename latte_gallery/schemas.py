from pydantic import BaseModel, StringConstraints
from typing import Literal, Annotated
from enum import StrEnum

class StatusResponse(BaseModel):
    status: Literal["ok"]

class KokResponse(BaseModel):
    kok: Literal["kok"]

class Role(StrEnum):
    USER = "USER"
    ADMIN = 'ADMIN'
    MAIN_ADMIN = 'MAIN_ADMIN'

class Account(BaseModel):
    id: int
    login: str
    name: str
    role: Role

class AccountRegister(BaseModel):
    login: Annotated[str, StringConstraints(min_length=1,strip_whitespace=True)]
    password: Annotated[str, StringConstraints(min_length=8)]
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
