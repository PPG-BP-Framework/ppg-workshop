"""Let pip install a checksum-verified wheel from a public Git repository."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import tarfile
from typing import Any


def _distribution() -> tuple[Path, dict[str, str]]:
    """Resolve the release manifest and verify the packaged wheel bytes."""
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "distribution.json").read_text(encoding="utf-8"))
    wheel = (root / manifest["wheel"]).resolve(strict=True)
    if not wheel.is_relative_to(root) or wheel.suffix != ".whl":
        raise ValueError("The manifest must reference a wheel within this repository.")
    if hashlib.sha256(wheel.read_bytes()).hexdigest() != manifest["sha256"]:
        raise ValueError("Wheel checksum does not match the release manifest.")
    return wheel, manifest


def build_wheel(
    wheel_directory: str,
    config_settings: dict[str, Any] | None = None,
    metadata_directory: str | None = None,
) -> str:
    """Return the original wheel; pip handles metadata, dependencies and installation."""
    wheel, _ = _distribution()
    destination = Path(wheel_directory)
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(wheel, destination / wheel.name)
    return wheel.name


def build_sdist(sdist_directory: str, config_settings: dict[str, Any] | None = None) -> str:
    """Archive the installer adapter and wheel if a frontend requests an sdist."""
    wheel, manifest = _distribution()
    root = Path(__file__).resolve().parent
    stem = f"{manifest['name']}-{manifest['version']}"
    destination = Path(sdist_directory)
    destination.mkdir(parents=True, exist_ok=True)
    filename = f"{stem}.tar.gz"
    with tarfile.open(destination / filename, "w:gz") as archive:
        for path in (root / "pyproject.toml", Path(__file__), root / "distribution.json", root / "README.md", wheel):
            archive.add(path, arcname=str(Path(stem) / path.relative_to(root)))
    return filename
