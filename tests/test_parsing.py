# tests/test_parsing.py
from src.parsing import Job

j = Job(id="x1", title="Apprenticeship/Trainee Opportunities", source="rss")
# Pydantic v2:
print(j.model_dump())