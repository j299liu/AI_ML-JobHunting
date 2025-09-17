from rapidfuzz import fuzz

def near_duplicate(a: dict, b: dict) -> bool:
    t = fuzz.token_sort_ratio(a.get("title",""), b.get("title",""))
    u = fuzz.token_sort_ratio(a.get("url",""), b.get("url",""))
    return (t > 90 and u > 70)