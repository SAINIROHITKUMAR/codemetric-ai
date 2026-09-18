import ast
from app.analyzer.complexity import complexity_metrics
from app.analyzer.maintainability import maintainability_metrics
from app.analyzer.quality import quality_score, suggestions

def analyze_code(code):
    tree = ast.parse(code)

    lines = code.splitlines()
    loc = sum(1 for line in lines if line.strip())
    blank_lines = sum(1 for line in lines if not line.strip())
    comments = sum(1 for line in lines if line.strip().startswith("#"))
    functions = sum(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                    for node in ast.walk(tree))
    classes = sum(isinstance(node, ast.ClassDef) for node in ast.walk(tree))
    imports = sum(isinstance(node, (ast.Import, ast.ImportFrom))
                  for node in ast.walk(tree))

    comment_ratio = round(comments / loc, 3) if loc else 0

    result = {
        "code": {
            "loc": loc,
            "blank_lines": blank_lines,
            "comments": comments,
            "comment_ratio": comment_ratio,
            "functions": functions,
            "classes": classes,
            "imports": imports
        },
        "complexity": complexity_metrics(code),
        "maintainability": maintainability_metrics(code)
    }

    result["quality_score"] = quality_score(result)
    result["suggestions"] = suggestions(result)
    return result
