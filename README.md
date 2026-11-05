# Project 3

Python project using a `src` layout.

## Getting started

Activate the existing virtual environment in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the project in editable mode:

```powershell
python -m pip install -e .
```

The Python package lives in `src/project3/`. Add application code there. Put automated checks in `tests/`.

## Project layout

```text
project3/
├── src/project3/       # Application package
├── tests/              # Tests
├── pyproject.toml      # Project metadata and build settings
├── .gitignore          # Files Git should ignore
└── README.md
```

## Working with Codex

Ask for one concrete task at a time, for example: “Explain this file”, “Add input validation to …”, or “Review the changes for bugs”. I can inspect and edit project files, explain Python or Git concepts, help debug errors you paste or run, and prepare commits or GitHub changes. I’ll describe important edits and can show diffs before you commit or publish them.

You stay in control of decisions like what the app should do and whether work should be committed or pushed. Mention constraints such as “keep it beginner-friendly” or “don’t change the public API” when they matter. For coding tasks, tell me the expected behavior and how you’ll know it works.

Useful Git commands:

```powershell
git status
git add .
git commit -m "Describe the change"
git push
```
