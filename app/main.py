from contextlib import asynccontextmanager
from sqlite3 import OperationalError
from fastapi import FastAPI
from app.database.connection import init_db, SessionLocal


app = FastAPI()

async def startup():
    try:
        print("Application starting...")
        session = SessionLocal()
        init_db()
        print("Database successfully connected. Application running.")
    except OperationalError as e:
        raise RuntimeError("Database connection failed.: {e}") from e
    
async def shutdown():
    print("Application shutting down...")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    yield
    await shutdown()

app = FastAPI(
    title="Task Manager Backend",
    description="Backend for a Task Management application",
    version="1.0.0",
    lifespan=lifespan
)