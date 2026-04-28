# Use cmd on Windows, sh on macOS and Linux
set windows-shell := ["powershell", "-NoProfile", "-Command"]

# Rendered output directory — gitignored, throwaway
rendered := ".rendered"
copier_source := ".copier-source"

# Render the template and run all checks against the output
# This mirrors exactly what CI does
# Usage: just check
check: render
    uv --directory {{rendered}} sync --all-groups --quiet
    uv --directory {{rendered}} run ruff format --check .
    uv --directory {{rendered}} run ruff check src tests
    uv --directory {{rendered}} run mypy src tests
    uv --directory {{rendered}} run pytest -q
    uv --directory {{rendered}} build --quiet

# Render the template only, without running checks
# Useful for inspecting the rendered output directly
# Usage: just render
render:
    uv run python -c "from pathlib import Path; import shutil; [shutil.rmtree(p) for p in (Path('{{rendered}}'), Path('{{copier_source}}')) if p.exists()]; s = Path('{{copier_source}}'); s.mkdir(); shutil.copy2('copier.yaml', s / 'copier.yaml'); shutil.copytree('template', s / 'template')"
    uvx copier copy {{copier_source}} {{rendered}} --defaults --overwrite --quiet
    uv run python -c "from pathlib import Path; import shutil; p = Path('{{copier_source}}'); shutil.rmtree(p) if p.exists() else None"

# Remove the rendered output directory
# Usage: just clean
clean:
    uv run python -c "from pathlib import Path; import shutil; [shutil.rmtree(p) for p in (Path('{{rendered}}'), Path('{{copier_source}}')) if p.exists()]"
