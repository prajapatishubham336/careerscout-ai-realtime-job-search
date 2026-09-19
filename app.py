import os
import json
import re

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from groq import Groq
from tavily import TavilyClient
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(title="CareerScout AI")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


class ChatRequest(BaseModel):
    message: str
    offset: int = 0


def extract_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", text)

        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass

    return {
        "summary": "Could not structure the search results.",
        "jobs": []
    }


def live_search(query, offset=0):
    groq_key = os.getenv("GROQ_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")

    if not groq_key:
        raise Exception("GROQ_API_KEY is missing.")

    if not tavily_key:
        raise Exception("TAVILY_API_KEY is missing.")

    tavily = TavilyClient(api_key=tavily_key)

    search_query = f"""
    Current job vacancies and internships for:
    {query}

    Search real job listings from company career pages,
    LinkedIn, Indeed, Internshala, Wellfound and other job portals.
    Prefer recent and directly applicable opportunities.
    """

    search_results = tavily.search(
        query=search_query,
        search_depth="advanced",
        topic="general",
        max_results=10,
        include_answer=False,
        include_raw_content=False
    )

    results = search_results.get("results", [])

    if not results:
        return {
            "summary": "No matching live job listings were found.",
            "jobs": []
        }

    compact_results = []

    for item in results:
        compact_results.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", "")
        })

    client = Groq(api_key=groq_key)

    extraction_prompt = f"""
You are CareerScout AI.

User request:
{query}

Live web search results:
{json.dumps(compact_results, ensure_ascii=False)}

Convert only the relevant job or internship listings into JSON.

Return ONLY valid JSON in this exact format:

{{
  "summary": "short useful summary",
  "jobs": [
    {{
      "company": "company name or Unknown",
      "title": "job title",
      "location": "location",
      "type": "Job or Internship",
      "experience": "experience requirement or Not specified",
      "skills": "important skills or Not specified",
      "description": "short description",
      "apply_url": "URL from the search results"
    }}
  ]
}}

Strict rules:
- Return maximum 10 jobs.
- Use only URLs provided in the search results.
- Do not invent companies, jobs or URLs.
- Exclude articles, courses, videos and generic career advice pages.
- Exclude results that are not related to the user's request.
- Prefer direct application pages.
- If the company is not clearly mentioned, use "Unknown".
- If fewer than 10 valid jobs exist, return fewer.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": extraction_prompt
            }
        ],
        response_format={"type": "json_object"},
        max_completion_tokens=3000,
        reasoning_effort="low"
    )

    content = response.choices[0].message.content or "{}"

    return extract_json(content)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/api/chat")
async def chat(body: ChatRequest):
    try:
        data = live_search(body.message, body.offset)
        jobs = data.get("jobs", [])

        return {
            "message": data.get(
                "summary",
                "Here are the latest matching opportunities."
            ),
            "jobs": jobs[:10],
            "has_more": len(jobs) >= 10
        }

    except Exception as e:
        print("ERROR:", repr(e))

        return {
            "message": f"Live search error: {str(e)}",
            "jobs": [],
            "has_more": False
        }