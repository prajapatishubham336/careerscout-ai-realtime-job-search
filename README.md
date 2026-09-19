# careerscout-ai-realtime-job-search
CareerScout AI is an AI-powered real-time job and internship discovery chatbot that uses Tavily live web search and Groq LLMs to find, filter, and present relevant career opportunities based on role, location, experience, and job type.


# 🔎 CareerScout AI

**![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![Tavily](https://img.shields.io/badge/Tavily-Live%20Web%20Search-blue)
![Jinja2](https://img.shields.io/badge/Jinja2-Templates-B41717)
![License](https://img.shields.io/badge/License-MIT-green)**

> An AI-powered real-time career discovery assistant that searches live job and internship opportunities based on user requirements such as role, location, experience level, and employment type.

---

## 🚀 Overview

Finding relevant jobs and internships across multiple platforms can be time-consuming.

**CareerScout AI** simplifies the job-search process through a conversational interface where users can enter natural-language queries such as:

- `Data Scientist jobs in Mumbai for fresher`
- `AI ML internship in Pune`
- `GenAI and LLM jobs in Bangalore`
- `Remote Data Analyst internship`
- `Python Developer jobs for 1 year experience`

The application uses **Tavily live web search** to retrieve current web results and **Groq LLM** to convert those results into structured job opportunity cards.

---

## ✨ Features

- 🔍 Real-time web-based job and internship search
- 🤖 AI-powered natural-language query understanding
- 📍 Location-based job discovery
- 🎓 Fresher and entry-level opportunity filtering
- 💼 Job and internship classification
- 🏢 Company name and job title extraction
- 🛠️ Skills and experience requirement extraction
- 🔗 Application URL display
- 🧾 Structured job cards for easy reading
- 🔄 Show more opportunities functionality
- 💬 Conversational chatbot interface
- 📱 Responsive and clean user interface
- ⚡ FastAPI-powered backend
- 🔐 API keys managed through environment variables

---

## 🧠 How It Works

```text
User enters a career-related query
                │
                ▼
       FastAPI Backend
                │
                ▼
       Tavily Live Web Search
                │
                ▼
      Relevant Search Results
                │
                ▼
         Groq LLM Processing
                │
                ▼
       Structured JSON Response
                │
                ▼
       Job Opportunity Cards
                │
                ▼
       User Views Application Links
```

---

## 🏗️ Architecture

```text
CareerScout AI
│
├── Frontend
│   ├── HTML
│   ├── CSS
│   └── JavaScript
│
├── Backend
│   └── FastAPI
│
├── Live Search Layer
│   └── Tavily Search API
│
├── AI Processing Layer
│   └── Groq LLM
│
└── Response Format
    └── Structured JSON Job Listings
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API framework |
| Uvicorn | ASGI server |
| Jinja2 | HTML template rendering |
| HTML | Frontend structure |
| CSS | User interface styling |
| JavaScript | Frontend interaction and API requests |
| Tavily API | Live web search |
| Groq API | AI-powered result extraction |
| Pydantic | Request validation |
| python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
careerscout_ai_realtime/
│
├── app.py
├── requirements.txt
├── .env
├── .env.example
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── app.js
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/prajapatishubham336/careerscout-ai-realtime-job-search.git
```

Move into the project directory:

```bash
cd careerscout-ai-realtime-job-search
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Required API Services

- Groq API: Used for AI-based processing and structured response generation.
- Tavily API: Used for live web search and retrieving current online information.

> Never upload your actual `.env` file or expose API keys publicly on GitHub.

---

## 📄 `.env.example`

Create a `.env.example` file with the following content:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## ▶️ Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn app:app --reload
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

---

## 💬 Example Queries

Try the following queries inside the chatbot:

```text
Data Scientist jobs in Mumbai for fresher
```

```text
AI ML internship in Pune
```

```text
GenAI and LLM jobs in Bangalore
```

```text
Remote Data Analyst internship
```

```text
Python Developer jobs in Hyderabad
```

---

## 📋 Job Information Displayed

CareerScout AI attempts to present the following information for each opportunity:

- Company name
- Job title
- Location
- Job or internship type
- Experience requirement
- Required skills
- Short job description
- Application URL

The displayed information depends on the availability and quality of the live search results.

---

## 🔌 API Endpoint

### Chat Endpoint

```http
POST /api/chat
```

### Request Body

```json
{
  "message": "GenAI jobs in Bangalore",
  "offset": 0
}
```

### Response Format

```json
{
  "message": "Matching career opportunities found.",
  "jobs": [
    {
      "company": "Example Company",
      "title": "Generative AI Engineer",
      "location": "Bangalore",
      "type": "Job",
      "experience": "0-2 years",
      "skills": "Python, LLM, RAG",
      "description": "Work on generative AI applications.",
      "apply_url": "https://example.com/job"
    }
  ],
  "has_more": false
}
```

---

## 🔒 Security Considerations

- API keys are stored in environment variables.
- Secret keys should never be committed to GitHub.
- Add `.env` to `.gitignore`.
- Search results should be validated before being displayed.
- Application URLs should originate from retrieved search results.
- The system should not fabricate companies, jobs, or application links.

---

## ⚠️ Limitations

- Search results depend on the Tavily API and available web pages.
- Some results may link to job portals instead of direct company application pages.
- Job availability can change after the search is performed.
- Search results may contain incomplete information.
- The number of available results depends on the search query and API limits.
- Users should verify job details on the official application page before applying.

---

## 🔮 Future Enhancements

- Advanced duplicate job detection
- Dedicated job APIs such as Adzuna or Jooble
- User authentication and saved searches
- Email alerts for new opportunities
- Resume-based job matching
- Skill-gap analysis
- Personalized job recommendations
- Salary and experience filtering
- Company rating and review integration
- Job application tracking dashboard
- Multi-language query support
- Scheduled job notifications

---

## 🎯 Use Cases

CareerScout AI can be useful for:

- Students searching for internships
- Freshers looking for entry-level jobs
- Professionals exploring career opportunities
- Developers searching for technical roles
- Data science and AI/ML aspirants
- Users searching for location-specific vacancies
- Candidates looking for remote opportunities

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add new feature"
```

5. Push the branch.

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project according to the terms of the license.

---

## 👨‍💻 Author

**Shubham Prajapati**

GitHub: [prajapatishubham336](https://github.com/prajapatishubham336)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
