from pydantic import BaseModel

class SubscriptionPlan(BaseModel):
    id: int
    name: str
    api_limit: int
    price: float
    renew_period: str