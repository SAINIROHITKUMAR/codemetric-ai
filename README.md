# CodeMetric AI

CodeMetric AI is an automated Python code quality assessment framework built with Python and Flask.

## Features

- Python source-code analysis
- Lines of code, comments, functions, classes and imports
- Cyclomatic complexity
- Maintainability Index
- Rule-based quality score
- Improvement suggestions
- REST API
- Simple browser dashboard
- Automated tests

## Project Structure

```text
codemetric-ai/
├── app/
│   ├── analyzer/
│   ├── utils/
│   ├── __init__.py
│   └── routes.py
├── examples/
├── frontend/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── run.py
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd codemetric-ai
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
python run.py
```

API:

- GET `/api/health`
- POST `/api/analyze`

Example request:

```json
{
  "code": "def add(a, b):\n    return a + b"
}
```

### 5. Open the dashboard

Open `frontend/index.html` in your browser while the Flask server is running.

## Testing

```bash
pytest
```

## Technologies

Python, Flask, REST API, AST, Radon, HTML, CSS, JavaScript, Pytest, Git and GitHub.

## Note

The quality score and suggestions are rule-based in this version. They are designed as an explainable baseline that can later be extended with an ML/LLM layer.
