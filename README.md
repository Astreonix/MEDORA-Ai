# MEDORA

MEDORA is a full-stack medical memory and care companion. The frontend is in `frontend/`; the deployable backend is the FastAPI service in `backend/`.

## Run the frontend

```powershell
cd frontend
npm install
npm run dev
```

## Run the FastAPI backend

For a local quick start, leave `DATABASE_URL` empty to use SQLite. For deployment, use PostgreSQL and set `DATABASE_URL`.

```powershell
cd backend
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Set `VITE_API_URL=http://localhost:8000` in `frontend/.env` to connect the frontend to the backend.

## Deployment

- Render uses the root [render.yaml](./render.yaml) and deploys the FastAPI service from `backend/`.
- Vercel uses [frontend/vercel.json](./frontend/vercel.json), with root directory `frontend`, build command `npm run build`, and output directory `dist`.
- Set `CORS_ORIGINS` on Render to the deployed Vercel URL.

AI Medical Memory and Care Companion

Folders: `frontend/` (React + Vite + Tailwind), `backend/` (FastAPI), `docs/`, `sample-data/`.
See `docs/MEDORA_Folder_Structure.pdf` for the full layout and the free setup checklist.
