from radon.metrics import mi_visit

def maintainability_metrics(code):
    score = round(mi_visit(code, multi=True), 2)
    if score >= 80:
        rating = "Excellent"
    elif score >= 60:
        rating = "Good"
    elif score >= 40:
        rating = "Moderate"
    else:
        rating = "Poor"
    return {"score": score, "rating": rating}
