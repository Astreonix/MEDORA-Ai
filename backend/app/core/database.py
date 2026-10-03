from collections.abc import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import settings


class Base(DeclarativeBase):
    
    pass


connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine_kwargs = {"connect_args": connect_args}
if settings.database_url.startswith("sqlite") and ":memory:" in settings.database_url:
    engine_kwargs["poolclass"] = StaticPool

engine = create_engine(settings.database_url, future=True, **engine_kwargs)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    from app.models import audit_log, chat_session, chunk, document, medical_event, user

    if settings.database_url.startswith("postgresql"):
        # Vercel can start several instances at the same time. PostgreSQL
        # advisory locking prevents concurrent CREATE TABLE statements from
        # colliding during cold starts.
        with engine.begin() as connection:
            connection.execute(text("SELECT pg_advisory_lock(hashtext('medora_schema_init'))"))
            try:
                Base.metadata.create_all(bind=connection)
            finally:
                connection.execute(
                    text("SELECT pg_advisory_unlock(hashtext('medora_schema_init'))")
                )
        return

    Base.metadata.create_all(bind=engine)