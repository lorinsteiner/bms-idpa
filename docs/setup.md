# Project Setup

This guide explains how to set up the `bms-idpa` project with all required dependencies and how to run its subprograms.

## 1. Prerequisites

This project uses **[uv](https://docs.astral.sh/uv/)** for Python version management, dependency resolution, and virtual environments, and requires **Python 3.14** (pinned in `.python-version`). To ensure consistent training and testing conditions for the experiments, we used the same Python and dependency versions throughout the project (see `uv.lock`).

If you do not have `uv` installed yet, install it first ([official uv installation guide](https://docs.astral.sh/uv/#installation)):

- **macOS / Linux:**

  ```sh
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

- **Windows (PowerShell):**

  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

> [!NOTE]
> You do not need to install Python 3.14 manually—`uv` will automatically download and use the version specified in `.python-version` during setup.

When you use Visual Studio Code, install following extensions for a complete development experience:

| Extension                         | Identifier                     |
| --------------------------------- | ------------------------------ |
| Python                            | ms-python.python               |
| Python Debugger                   | ms-python.debugpy              |
| Pyrefly - Python Language Tooling | meta.pyrefly                   |
| Prettier - Code formatter         | esbenp.prettier-vscode         |
| markdownlint                      | davidanson.vscode-markdownlint |

## 2. Clone the repository

Clone the repository from GitHub to your computer: [GitHub / bms-idpa](https://github.com/lorinsteiner/bms-idpa/).

## 3. Install Dependencies

1. Open a terminal in the project root directory (`bms-idpa`).
2. Sync the virtual environment and install all locked dependencies (including development dependencies such as `pytest`):

   ```sh
   uv sync
   ```

   This creates a `.venv` directory in the project root and installs all packages listed in `pyproject.toml` and `uv.lock`.

   If you only want to install runtime dependencies without development tools (e.g. `pytest`), run:

   ```sh
   uv sync --no-dev
   ```

For an overview of what each dependency is used for, see [dependencies.md](./dependencies.md).

## 4. Running the Subprograms

The project provides a single command-line interface, `idpa`, built with **[Typer](https://typer.tiangolo.com/)** and defined as a script entry point in `pyproject.toml`. Individual subprograms are exposed as Typer subcommands in `src/idpa/cli`:

| Subcommand | Entry Point                   | Command             | Description                                     |
| ---------- | ----------------------------- | ------------------- | ----------------------------------------------- |
| `main`     | `idpa.experiments.main:main`  | `uv run idpa main`  | Runs the main experiment.                       |
| `pilot`    | `idpa.experiments.pilot:main` | `uv run idpa pilot` | Runs the pilot experiment.                      |
| `dev`      | `idpa.dev.playground:dev`     | `uv run idpa dev`   | Development playground (development mode only). |

> [!NOTE]
> The `dev` subcommand is only available in development mode (when `pytest` is installed via `uv sync`). If you installed dependencies with `uv sync --no-dev`, the `dev` subcommand is hidden.

You can use Typer's built-in `--help` flag at any time to see all available subcommands or inspect a specific subcommand:

```sh
uv run idpa --help
uv run idpa <subcommand> --help
```

### Option A: Using `uv run` (Recommended)

`uv run` automatically uses the project's `.venv` without needing to activate it manually:

- **Run the `main` experiment:**

  ```sh
  uv run idpa main
  ```

- **Run the `pilot` experiment:**

  ```sh
  uv run idpa pilot
  ```

- **Run the `dev` playground (development mode only):**

  ```sh
  uv run idpa dev
  ```

### Option B: Activating the Virtual Environment

If you prefer to run the `idpa` CLI directly without prefixing `uv run`:

1. Activate `.venv`:
   - **macOS / Linux:**

     ```sh
     source .venv/bin/activate
     ```

   - **Windows (PowerShell):**

     ```powershell
     .venv\Scripts\Activate.ps1
     ```

2. Run any subcommand directly:

   ```sh
   idpa main
   idpa pilot
   idpa dev
   idpa --help
   ```

## 5. Running Automated Tests (`pytest`)

To run the `pytest` test suite (installed as part of the `dev` dependency group):

```sh
uv run pytest
```
