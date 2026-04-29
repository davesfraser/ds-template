# Use cmd on Windows, sh on macOS and Linux
set windows-shell := ["powershell", "-NoProfile", "-Command"]

# Rendered output directory — gitignored, throwaway
rendered := ".rendered"
copier_source := ".copier-source"

# Render the template and run all checks against the output
# This mirrors exactly what CI does
# Usage: just check
check: check-extension-markers render
    $env:VIRTUAL_ENV = $null; uv --directory {{rendered}} sync --all-groups --quiet
    $env:VIRTUAL_ENV = $null; uv --directory {{rendered}} sync --frozen --all-groups --quiet
    $env:VIRTUAL_ENV = $null; uv --directory {{rendered}} run ruff format --check .
    $env:VIRTUAL_ENV = $null; uv --directory {{rendered}} run ruff check src tests notebooks scripts
    $env:VIRTUAL_ENV = $null; uv --directory {{rendered}} run marimo check notebooks/marimo
    $env:VIRTUAL_ENV = $null; uv --directory {{rendered}} run mypy src tests
    $env:VIRTUAL_ENV = $null; uv --directory {{rendered}} run pytest -q
    $env:VIRTUAL_ENV = $null; uv --directory {{rendered}} build --quiet

# Verify downstream extension blocks are still present and well-formed
check-extension-markers:
    $env:VIRTUAL_ENV = $null; uv run python scripts/check_extension_markers.py

# Render the template only, without running checks
# Useful for inspecting the rendered output directly
# Usage: just render
render:
    uv run python -c "from pathlib import Path; import shutil; [shutil.rmtree(p) for p in (Path('{{rendered}}'), Path('{{copier_source}}')) if p.exists()]; s = Path('{{copier_source}}'); s.mkdir(); shutil.copy2('copier.yaml', s / 'copier.yaml'); shutil.copytree('template', s / 'template')"
    uv run python scripts/render_template.py {{copier_source}} {{rendered}}

# Remove the rendered output directory
# Usage: just clean
clean:
    $env:VIRTUAL_ENV = $null; uv run python -c "from pathlib import Path; import shutil; [shutil.rmtree(p) for p in (Path('{{rendered}}'), Path('{{copier_source}}')) if p.exists()]"
