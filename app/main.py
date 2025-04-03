from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Bugsy", description="Simple issue tracker microservice"
)
app.include_router(router)
