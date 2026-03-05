from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from .database import Base
    
class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    subscription_plans_id = Column(Integer, ForeignKey("subscription_plans.id"), default=1)
    joining_date = Column(DateTime, default=datetime.utcnow)


# Company has to buy plan from here, I'll set my plan and price    
class SubscriptionPlan(Base):
    __tablename__ = "subscription_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)  
    api_limit = Column(Integer)         
    price = Column(Float)
    renew_period= Column(String)   #daily, weekly, monthly
 
 
# Company can create thier own plan for api limit    
class ClientPlan(Base):
    __tablename__ = "client_plan"
   
    id = Column(Integer, primary_key=True, index=True)
    plan_name = Column(String)
    company_id = Column(Integer, ForeignKey("company.id"))  
    api_limit = Column(Integer)
    renew_period= Column(String)   #daily, weekly, monthly
    
    
class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("company.id"))
    api_key = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="active")  # active / revoked