import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_ticket(title, description):

    prompt = f"""
You are an AI Customer Support Assistant.

Analyze this ticket and respond ONLY as valid JSON.

Ticket Title:
{title}

Ticket Description:
{description}

Return EXACTLY this JSON format:

{{
    "summary": "...",
    "category": "Technical",
    "priority": "High",
    "reply": "..."
}}
"""

    response = model.generate_content(prompt)

    return response.text