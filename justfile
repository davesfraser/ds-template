# Use PowerShell on Windows, sh on macOS and Linux
# PowerShell handles quoted arguments correctly unlike cmd
set windows-shell := ["powershell", "-NoProfile", "-Command"]

# Rendered output directory — gitignored, throwaway
rendered := ".rendered"

# Render the template and run all checks against the output
# This mirrors exactly what CI does
# Usage: just check
check: render
    uv --directory {{rendered}} sync --all-groups --quiet
    uv --directory {{rendered}} run ruff format --check .
    uv --directory {{rendered}} run ruff check src tests notebooks
    uv --directory {{rendered}} run marimo check notebooks/marimo
    uv --directory {{rendered}} run mypy src tests
    uv --directory {{rendered}} run pytest -q
    uv --directory {{rendered}} build --quiet

# Render the template only, without running checks
# Useful for inspecting the rendered output directly
# Usage: just render
render:
    uv run python -c "import shutil; shutil.rmtree('.rendered', ignore_errors=True)"
    uvx copier copy . {{rendered}} --defaults --overwrite --quiet

# Remove the rendered output directory
# Usage: just clean
clean:
    uv run python -c "import shutil; shutil.rmtree('.rendered', ignore_errors=True)"
