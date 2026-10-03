from fastapi import APIRouter

from app.api.v1.endpoints import auth, brief, care, chat, compare, documents, simplifier, timeline

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(timeline.router, prefix="/timeline", tags=["timeline"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(brief.router, prefix="/brief", tags=["brief"])
api_router.include_router(care.router, prefix="/care", tags=["care"])
api_router.include_router(simplifier.router, prefix="/simplifier", tags=["simplifier"])
api_router.include_router(compare.router, prefix="/compare", tags=["compare"])