from fastapi import APIRouter
from curd.company_curd import add_company
from schemas.company_schema import Company

curd_routes = APIRouter()

@curd_routes.post("/addCompany")
def create_company(company: Company):
    return add_company(company)