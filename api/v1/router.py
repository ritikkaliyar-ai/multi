from fastapi import APIRouter

route = APIRouter()

@route.post('/test')
def test(name):
    return name