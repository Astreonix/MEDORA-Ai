# MEDORA Frontend

## Run locally

```bash
npm install
npm run dev
```

The frontend uses React, Vite, React Router, Tailwind tokens, and offline mock service functions. Use any email and a password of six or more characters to enter the demo workspace. Set `VITE_API_URL` in `.env` when connecting a future backend; current screens remain usable offline.

## Routes

`/`, `/login`, `/register`, `/dashboard`, `/upload`, `/documents`, `/documents/:documentId`, `/timeline`, `/ask-medora`, `/simplifier`, `/doctor-brief`, `/find-care`, `/compare`, `/story`

## Structure

- `src/components/` contains reusable UI and feature components.
- `src/pages/` assembles route-level screens.
- `src/services/` contains mock data and backend integration boundaries.
- `src/hooks/` contains stateful screen logic.
- `src/context/` contains authentication and language providers.
- `src/utils/` contains shared constants, formatting, and validation helpers.