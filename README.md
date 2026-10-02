# UWE MSc AI Platform

A full-stack community platform for UWE Bristol MSc Artificial Intelligence students, researchers, and alumni.

The platform enables students to:

- Discover AI events and workshops
- Share projects and research
- Access learning resources
- Connect with the AI community
- Build professional profiles
- Collaborate on research and development

---

## Tech Stack

### Frontend

- Next.js 15 (App Router)
- TypeScript
- Tailwind CSS
- Shadcn/UI
- Axios
- TanStack Query
- Zustand

### Backend

- FastAPI
- SQLAlchemy 2.x
- PostgreSQL
- Pydantic v2
- Alembic
- JWT Authentication

### DevOps

- Docker
- Docker Compose
- GitHub Actions

---

## Project Structure

```text
uwe-msc-ai-platform/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── dependencies/
│   │   ├── db/
│   │   └── main.py
│   ├── .env.example
│   ├── requirements.txt
│   ├── Dockerfile
│   └── alembic.ini
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   └── .env.example
├── docker-compose.yml
├── .gitignore
├── README.md
└── LICENSE
```

---

## Features

### Authentication

- User Registration
- User Login
- JWT Authentication
- Role-based access control

Roles:
- Student
- Researcher
- Alumni
- Admin

### Dashboard

Displays:
- Upcoming events
- Featured projects
- Community feed
- Latest resources

### Community

Students can:
- Create posts
- Share updates
- Comment
- Like discussions

### Events

Features:
- Event listings
- Registration
- Reminders
- RSVP management

### Projects

Students can:
- Showcase projects
- Request collaborators
- Add repository links
- Add documentation

### Resources

Students can share:
- Research papers
- Lecture notes
- Tutorials
- GitHub repositories
- Books

### Profiles

Every user has:
- Name
- Degree program
- Skills
- Bio
- LinkedIn
- GitHub
- Portfolio
- Contributions

---

## Quick Start

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

### Docker

```bash
docker compose up --build
```

---

## Default URLs

- Backend: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- Frontend: `http://localhost:3000`

---

## License

MIT License

---

## Author

Bilal Abdulkadir Muhammed

- GitHub: [@Bilalabdulkadir](https://github.com/Bilalabdulkadir)
- LinkedIn: [Bilal Abdulkadir](https://linkedin.com/in/bilalabdulkadir)
- Portfolio: [bilalabdulkadir.github.io](https://bilalabdulkadir.github.io)
- ORCID: [0009-0007-8605-6281](https://orcid.org/0009-0007-8605-6281)

UWE Bristol MSc Artificial Intelligence
