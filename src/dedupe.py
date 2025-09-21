# decide if two job postings are essentially the same, even if their text is slightly different.
from rapidfuzz import fuzz

def near_duplicate(a: dict, b: dict) -> bool:
    t = fuzz.token_sort_ratio(a.get("title",""), b.get("title",""))
    c = fuzz.token_sort_ratio(a.get("company",""), b.get("company",""))
    l = fuzz.token_sort_ratio(a.get("location",""), b.get("location",""))
    u = fuzz.token_sort_ratio(a.get("url",""), b.get("url",""))
    
    # Title high + (company or location high) → duplicate
    if t >= 95 and c >= 80 and l >= 50:
        return True
    # Fallback to URL similarity if titles are high
    if t >= 95 and u > 70:
        return True
    return False