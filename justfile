
dev:
  uv run python runner.py

make-requirements:
  uv pip compile pyproject.toml -o requirements.txt
