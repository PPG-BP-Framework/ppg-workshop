# Teaching repository and private runtime

- Public teaching materials: https://github.com/PPG-BP-Framework/ppg-workshop
- Private pip runtime: https://github.com/mamerm/ppg-workshop-runtime

Participants can read/download these notebooks and configs without authentication.
To run them, the instructor grants each participant access to the private runtime
repository. Follow README.md for Git authentication and the exact pip command.
Installation also bundles both notebooks; `ppg-workshop init ./my-ppg-workshop`
generates them and their task folders without a manual repository download.

The runtime has CPython 3.11 bytecode instead of readable framework source modules.
This discourages casual inspection but does not prevent reverse engineering.
The public teaching repository contains neither that wheel nor the older readable
source wheels. It has a fresh history, independent of older instructor repositories.

## Upload future teaching changes

Edit this repository's notebooks, configs or documents, then review the files:

```sh
git status
git diff
```

Stage only intended teaching changes, commit them, then run `git push origin main`.
Do not add private wheels, source archives, data, weights, executed notebooks or
local results. The supplied .gitignore excludes those artifact folders.

## Export an environment

Run `python export_environment.py` inside the activated workshop environment.
The generated environment.exported.yml removes the machine prefix and uses the
version-pinned private installer URL. It remains platform-specific. Recreating it
requires Git authentication and access to the runtime repository.
