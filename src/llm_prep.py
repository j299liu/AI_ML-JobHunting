import os

SYSTEM_PROMPT = """
You are my ML Job Scout for UK roles. Parse a job and output:
- 3 tailored CV bullets (impact-led, with metrics)
- 6–10 keywords to mirror
- 3-sentence message to hiring contact referencing one concrete requirement
Use UK spelling. Keep it concise.
"""

def build_user_prompt(job: dict, cluster: str, my_bullets: list) -> str:
    # Condense the article’s cluster-specific prompts into one dynamic prompt. :contentReference[oaicite:7]{index=7}
    base = f"""Job:
Title: {job.get('title')}
Company: {job.get('company')}
Location: {job.get('location')}
Link: {job.get('url')}
Snippet: {job.get('snippet')}

My background bullets:
- """ + "\n- ".join(my_bullets) + f"""

Cluster: {cluster}
"""
    return base

def generate_with_llm(prompt: str) -> dict:
    # Placeholder: plug in your provider (OpenAI/Azure/OpenAI, etc.)
    # return {"cv_bullets":[...], "keywords":[...], "message":"..."}
    return {}