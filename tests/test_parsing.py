# tests/test_parsing.py
from src.parsing import Job

j = Job(id="x1", title="Apprenticeship/Trainee Opportunities", source="rss")
# Pydantic v2:
print(j.model_dump())

# {'id': 'x1', 'title': 'Apprenticeship/Trainee Opportunities', 'company': None, 'location': None, 'url': None, 'source': 'rss', 'published_at': None, 'snippet': Nong None, 'cluster': None, 'score': None}