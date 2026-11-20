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

The project defines its subprograms as script entry points in `pyproject.toml` (`[project.scripts]`):

| Subprogram | Entry Point         | Command          |
| ---------- | ------------------- | ---------------- |
| `pretest`  | `idpa.pretest:main` | `uv run pretest` |
| `test`     | `idpa.test:main`    | `uv run test`    |

### Option A: Using `uv run` (Recommended)

`uv run` automatically uses the project's `.venv` without needing to activate it manually:

- **Start `pretest`:**
  ```sh
  uv run pretest
  ```
- **Start `test`:**
  ```sh
  uv run test
  ```

### Option B: Activating the Virtual Environment

If you prefer to run the commands directly without prefixing `uv run`:

1. Activate `.venv`:
   - **macOS / Linux:**
     ```sh
     source .venv/bin/activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
2. Run the subprograms directly:
   ```sh
   pretest
   test
   ```

## 5. Running Automated Tests (`pytest`)

To run the `pytest` test suite (installed as part of the `dev` dependency group):

```sh
uv run pytest
```
