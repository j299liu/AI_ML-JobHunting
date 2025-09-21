# tests/test_cluster_score.py
from src.cluster_score import assign_cluster, score_fit

text = "Trainee. Remote UK."
cluster = assign_cluster(text)
score = score_fit(
    text,
    profile_skills=[],
    locations_ok=["Remote UK","Newcastle"]
)
print(cluster, score)

# Trainee 5.019