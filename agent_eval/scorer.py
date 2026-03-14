import difflib


def score(actual: str, expected: str, method: str = "semantic_similarity", threshold: float = 0.85) -> dict:
    """Score actual output against expected."""
    if method == "exact_match":
        passed = actual.strip().lower() == expected.strip().lower()
        return {"method": method, "passed": passed, "score": 1.0 if passed else 0.0}

    elif method == "contains":
        passed = expected.lower() in actual.lower()
        return {"method": method, "passed": passed, "score": 1.0 if passed else 0.0}

    elif method == "semantic_similarity":
        # Use difflib as lightweight fallback (no heavy ML deps required)
        similarity = difflib.SequenceMatcher(None, actual.lower(), expected.lower()).ratio()
        passed = similarity >= threshold
        return {"method": method, "score": round(similarity, 4), "threshold": threshold, "passed": passed}

    return {"method": method, "passed": False, "score": 0.0, "error": f"Unknown method: {method}"}
