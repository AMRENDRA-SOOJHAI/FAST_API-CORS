"""Database configuration and session management for FastAPI application."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./Orders.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    bind=engine, autocommit=False, autoflush=False
)

Base = declarative_base()

# Dependency
def get_db():
    """
    FastAPI dependency to provide database session.
    
    Yields:
        SQLAlchemy Session instance for database operations.
        
    Ensures session is properly closed after request completion.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
