def quality_score(metrics):
    score = 100.0

    complexity = metrics["complexity"]["average_complexity"]
    if complexity > 10:
        score -= 25
    elif complexity > 5:
        score -= 12

    mi = metrics["maintainability"]["score"]
    if mi < 40:
        score -= 30
    elif mi < 60:
        score -= 15
    elif mi < 80:
        score -= 5

    comment_ratio = metrics["code"]["comment_ratio"]
    if metrics["code"]["loc"] >= 20 and comment_ratio < 0.05:
        score -= 5

    return max(0, round(score, 2))

def suggestions(metrics):
    result = []
    if metrics["complexity"]["average_complexity"] > 10:
        result.append("Break complex functions into smaller functions.")
    elif metrics["complexity"]["average_complexity"] > 5:
        result.append("Consider simplifying functions with high branching.")
    if metrics["maintainability"]["score"] < 60:
        result.append("Improve maintainability by reducing complexity and duplication.")
    if metrics["code"]["loc"] >= 20 and metrics["code"]["comment_ratio"] < 0.05:
        result.append("Add useful comments or docstrings where they improve clarity.")
    if not result:
        result.append("No major issues detected by the current rule set.")
    return result
