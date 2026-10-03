# MEDORA Frontend

## Run locally

```bash
npm install
npm run dev
```

The frontend uses React, Vite, React Router, Tailwind tokens, and the deployed FastAPI backend. Set `VITE_API_URL` in `.env` to the API origin (without `/api/v1`) before running locally. Registration and login require a password of at least eight characters.

## Routes

`/`, `/login`, `/register`, `/dashboard`, `/upload`, `/documents`, `/documents/:documentId`, `/timeline`, `/ask-medora`, `/simplifier`, `/doctor-brief`, `/find-care`, `/compare`, `/story`

## Structure

- `src/components/` contains reusable UI and feature components.
- `src/pages/` assembles route-level screens.
- `src/services/` contains API clients and backend integration boundaries.
- `src/hooks/` contains stateful screen logic.
- `src/context/` contains authentication and language providers.
- `src/utils/` contains shared constants, formatting, and validation helpers.