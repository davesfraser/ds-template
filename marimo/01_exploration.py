# marimo is our notebook-style workflow
# Unlike .ipynb files, this stays as normal Python code in git
import marimo as mo

# A marimo app is made of reactive cells, uses decorators to denote where they start / end
app = mo.App()


@app.cell
def _():
    # Starter variable for the next cell to use
    name = "world"
    return name


@app.cell
def _(name):
    # Show markdown output in the notebook/app
    mo.md(f"# Hello, {name}!")
    return


# Normal Python entry point
# Lets the file be run directly
if __name__ == "__main__":
    app.run()
