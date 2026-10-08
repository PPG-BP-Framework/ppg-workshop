"""Execute a participant notebook in its own workspace with an installed kernel."""

from __future__ import annotations

import argparse
from pathlib import Path

import nbformat
from nbclient import NotebookClient


def main() -> None:
    """Run every notebook cell and retain outputs even when a cell fails."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notebook", required=True, type=Path)
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--kernel", default="ppg-workshop-showcase")
    parser.add_argument("--timeout", type=int, default=1800)
    args = parser.parse_args()
    notebook = nbformat.read(args.notebook, as_version=4)

    def started(cell: dict, cell_index: int, **kwargs: object) -> None:
        if cell["cell_type"] == "code":
            print(f"Executing cell {cell_index}: {cell['source'].splitlines()[0]}", flush=True)

    client = NotebookClient(notebook, timeout=args.timeout, kernel_name=args.kernel,
                            resources={"metadata": {"path": str(args.workspace.resolve())}},
                            on_cell_start=started)
    try:
        client.execute()
    finally:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        nbformat.write(notebook, args.output)
    print(f"Completed all cells: {args.output}", flush=True)


if __name__ == "__main__":
    main()
