# Reference API

- `GET /health`, `GET /ready`
- `GET /api/projects`
- `POST /api/projects` (admin token)
- `GET /api/projects/{id}`
- `POST /api/projects/{id}/claims` (admin token)
- `POST /api/projects/{id}/gaps` (admin token)
- `POST /api/projects/{id}/responses` (admin token)
- `GET /api/projects/{id}/report`
- `GET /api/projects/{id}/rti`
- `GET /api/projects/{id}/audit` (admin token)

Reference mode uses `Authorization: Bearer <ADMIN_TOKEN>`. Production must replace this with OIDC/MFA and role checks.
