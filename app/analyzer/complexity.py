import ast
from radon.complexity import cc_visit

def complexity_metrics(code):
    blocks = cc_visit(code)
    complexities = [
        {
            "name": block.name,
            "type": block.classname,
            "complexity": block.complexity,
            "rank": block.rank()
        }
        for block in blocks
    ]
    total = sum(item["complexity"] for item in complexities)
    average = round(total / len(complexities), 2) if complexities else 1.0
    return {
        "total_complexity": total,
        "average_complexity": average,
        "blocks": complexities
    }
