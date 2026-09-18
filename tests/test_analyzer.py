from app.analyzer.metrics import analyze_code

def test_analyze_code():
    code = """
def add(a, b):
    return a + b
"""
    result = analyze_code(code)
    assert result["code"]["functions"] == 1
    assert result["code"]["loc"] == 2
    assert 0 <= result["quality_score"] <= 100
