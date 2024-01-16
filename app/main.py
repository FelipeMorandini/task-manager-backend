from contextlib import asynccontextmanager
from sqlite3 import OperationalError
from fastapi import FastAPI
from app.database.connection import close_db_connection, init_db, SessionLocal


app = FastAPI(
    title="Task Manager Backend",
    description="Backend for a Task Management application",
    version="1.0.0",
)

def create_app() -> FastAPI:
    app = FastAPI(
        title="Task Manager Backend",
        description="Backend for a Task Management application",
        version="1.0.0",
    )
    
    # app.include_router(router)

    app.add_event_handler("startup", init_db)
    app.add_event_handler("shutdown", close_db_connection)

    return app

app = create_app()