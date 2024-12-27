from fastapi import FastAPI
from handlers import routers

app = FastAPI()

for handler in routers:
    app.include_router(handler)
