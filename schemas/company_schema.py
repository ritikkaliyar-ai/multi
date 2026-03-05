from pydantic import BaseModel, Field
from datetime import datetime


class Company(BaseModel):
    id: int = Field(...)
    name: str
    subscription_plans_id: int
    joining_date: datetime