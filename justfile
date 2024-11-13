
run:
  uv run python src/runner.py

make-requirements:
  uv pip compile pyproject.toml -o requirements.txt
