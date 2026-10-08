# One public workshop repository

https://github.com/PPG-BP-Framework/ppg-workshop contains the teaching notebooks,
configuration, environment/setup scripts and the compiled framework wheel.
No other repository or participant authentication is required.

After cloning, install with `python -m pip install ".[workshop]"`. Alternatively,
use the versioned public Git pip command in README.md. `distribution.json` identifies
the included wheel and checksum; `wheel_backend.py` returns that verified wheel to pip.

For updates, commit intended teaching changes and push to main. New runtime versions
need a new wheel, manifest, installation.json and Git tag; do not replace an existing
tag's artifact. Keep datasets, weights, temporary outputs and source wheels out of Git.
Only the intended CPython bytecode runtime belongs in artifacts/.

Run `python export_environment.py` to export the active environment with the public
installer URL. Environment snapshots remain platform-specific. Nothing uses a private
installer or requires GitHub login.
