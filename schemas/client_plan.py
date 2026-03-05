from pydantic import BaseModel

class ClientPlan(BaseModel):
    
    id: int
    plam_name: str
    api_limit: int
    company_id: int
    renew_period: str