"""Export the active conda environment without publishing machine-specific paths."""

from __future__ import annotations

import argparse
from importlib.metadata import version
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import yaml


def export_environment(*, conda: str, output: Path, name: str) -> None:
    """Save a platform-specific snapshot with an authenticated private pip requirement."""
    result = subprocess.run(
        [conda, "env", "export", "--prefix", sys.prefix, "--no-builds", "--json"],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    specification = json.loads(result.stdout)
    specification.pop("prefix", None)
    specification["name"] = name
    specification["channels"] = ["conda-forge", "nodefaults"]
    package = "ppg-experiment-framework"
    installation = json.loads(Path(__file__).with_name("installation.json").read_text(encoding="utf-8"))
    framework_requirement = f"{package}[workshop] @ git+{installation['repository_url']}@v{version(package)}"
    pip_requirements = []
    conda_requirements = []
    for dependency in specification["dependencies"]:
        if isinstance(dependency, dict):
            for requirement in dependency.get("pip", []):
                dependency_name = requirement.split("==")[0].split(" @ ")[0]
                if dependency_name.lower().replace("_", "-") == package:
                    continue
                if " @ " in requirement:
                    requirement = f"{dependency_name}=={version(dependency_name)}"
                if requirement.startswith("-e ") or "file:" in requirement:
                    raise ValueError(f"Unportable dependency: {dependency_name}")
                pip_requirements.append(requirement)
        else:
            conda_requirements.append(dependency)
    if sys.platform == "win32" and "+cpu" in version("torch"):
        pip_requirements.insert(0, "--extra-index-url https://download.pytorch.org/whl/cpu")
    specification["dependencies"] = conda_requirements + [{"pip": pip_requirements + [framework_requirement]}]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(yaml.safe_dump(specification, sort_keys=False), encoding="utf-8")
    print(f"Exported {output}. Recreate from the workshop folder on the same platform.")


def main() -> None:
    """Parse the conda executable, environment name and output destination."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--conda", default=os.environ.get("CONDA_EXE") or shutil.which("conda"))
    parser.add_argument("--output", type=Path, default=Path("environment.exported.yml"))
    parser.add_argument("--name", default="ppg_workshop_showcase")
    args = parser.parse_args()
    if not args.conda:
        parser.error("Activate conda first, or pass --conda PATH_TO_CONDA.")
    export_environment(conda=args.conda, output=args.output, name=args.name)


if __name__ == "__main__":
    main()
