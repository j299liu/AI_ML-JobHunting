from typing import Dict, Tuple
from rapidfuzz import fuzz

# Keyword map adapted from the article’s clusters (trim/add as needed)
CLUSTERS: Dict[str, Tuple[set, set]] = {
    "LLM/NLP": ({"LLM","NLP","Generative","Transformers","Hugging Face","RAG","LoRA","vLLM"}, {"PyTorch","JAX","TensorFlow"}),
    "Vision": ({"Computer Vision","Perception","OpenCV","segmentation","detection","TensorRT","OpenVINO"}, {"PyTorch","TensorFlow"}),
    "Core ML": ({"scikit-learn","XGBoost","LightGBM","CatBoost","SHAP","monitoring"}, {"Python","FastAPI"}),
    "Recs": ({"Recommender","Ranking","two-tower","bandit","ANN","Faiss","NDCG","MAP"}, set()),
    "MLOps": ({"Kubernetes","KServe","Seldon","BentoML","MLflow","registry","feature store","Kubeflow","Airflow","Prefect"}, {"Docker","CI/CD"}),
    "Distributed/Perf": ({"CUDA","DeepSpeed","FSDP","ZeRO","NCCL","mixed precision","Triton","XLA"}, set()),
    "Research": ({"pretraining","fine-tuning","benchmark","SOTA","open source"}, {"PyTorch","JAX"}),
    "Edge": ({"ONNX","TensorRT-LLM","OpenVINO","Core ML","TFLite","quantisation","pruning"}, set()),
}

def assign_cluster(text: str) -> str:
    t = text.lower()
    best, score = None, -1
    for c, (kw, _) in CLUSTERS.items():
        s = sum(1 for k in kw if k.lower() in t)
        if s > score:
            best, score = c, s
    return best or "Other"

def score_fit(text: str, profile_skills: list, locations_ok: list) -> float:
    t = text.lower()
    skill_hits = sum(1 for s in profile_skills if s.lower() in t)
    loc_bonus = 5 if any(loc.lower() in t for loc in locations_ok) else 0
    length_bonus = min(len(text) / 1000, 5)  # light heuristic
    return min(100, 10*skill_hits + loc_bonus + length_bonus)