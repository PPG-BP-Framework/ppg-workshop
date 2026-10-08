# PPG-DaLiA workshop

An installed-library workshop: formatting, signal processing, HDF5 I/O,
subject splits, training-only normalization, torch MLP training, frozen
PaPaGei-S with a trained head, and held-out error analysis.

## What this repository contains

This is the public teaching repository: both Jupyter notebooks, editable configs,
task templates and environment setup instructions. It contains no framework wheel,
framework implementation, raw dataset or pretrained weights.

**Both notebooks are also included in the private pip package.** After installing,
`ppg-workshop init ./my-ppg-workshop` writes `workshop_cpu_short.ipynb`,
`workshop.ipynb`, the configs and task folders to your computer. You can therefore
follow this README without cloning this repository.

## Choose a notebook

- `workshop_cpu_short.ipynb`: recommended live session. Six subjects x two minutes,
  two outer folds, five epochs per candidate, live learning curves, a two-candidate
  worked grid search, a separate editable participant grid block, optional frozen
  PaPaGei and Integrated Gradients on a selected held-out window.
- `workshop.ipynb`: the complete reference tour, including advanced data APIs.

Downloads must be completed before class. The short profile reduces processing
and training time, not the size of the original DaLiA download.

## Step-by-step setup and launch

**`pip install` does not create an environment.** Conda creates the environment;
activation selects it; `python -m pip install` puts the workshop library and its
dependencies into that active environment. The notebooks and saved-output examples
are already in this repository and remain unchanged.

### 1. Open a conda terminal

Install Miniconda or Anaconda if you do not already have it. On Windows, open
**Miniconda Prompt** or **Anaconda Prompt**. On macOS/Linux, use a terminal where
`conda` is initialized. Check:

```sh
conda --version
```

### 2. Create and activate the workshop environment

Use **CPython 3.11**, which is required by the compiled runtime:

```sh
conda create -n ppg_workshop_showcase --override-channels -c conda-forge python=3.11 pip git -y
conda activate ppg_workshop_showcase
python --version
```

The last command should report Python 3.11.x. If this environment already exists,
skip `conda create` and just activate it. Keep this terminal open for the next steps.

### 3. Get access and authenticate GitHub

Ask the instructor to grant your GitHub account access to
[mamerm/ppg-workshop-runtime](https://github.com/mamerm/ppg-workshop-runtime), and
accept the invitation. Authentication to the private runtime is needed even if you
clone the public teaching repository.

Authenticate Git using Git Credential Manager's sign-in flow, or, if you have
GitHub CLI installed, run:

```sh
gh auth login
gh auth setup-git
```

Verify that Git can access the runtime:

```sh
git ls-remote https://github.com/mamerm/ppg-workshop-runtime.git
```

Success prints Git references. If you see `Repository not found` or an authentication
error, check that you accepted the invitation and signed into the correct account.
Do not paste access tokens into notebooks or the install command.

### 4. Clone this repository and enter its folder

Run this from the parent folder where you want to keep the workshop:

```sh
git clone https://github.com/PPG-BP-Framework/ppg-workshop.git
cd ppg-workshop
```

If you already cloned it, enter that existing folder and run `git pull` instead.
Both `workshop.ipynb` and `workshop_cpu_short.ipynb` are immediately available,
along with `configs/`. There is no need to run `ppg-workshop init` for this route.

### 5. Install into the active environment

For the exact tested **Windows CPU** dependencies, run this first, from the cloned
folder (skip this platform-specific snapshot on macOS/Linux):

```sh
python -m pip install -r requirements-tested-windows-cpu.txt
```

Then install the workshop runtime and its notebook dependencies on any platform:

```sh
python -m pip install "ppg-experiment-framework[workshop] @ git+https://github.com/mamerm/ppg-workshop-runtime.git@v0.1.3"
python -m pip check
```

`pip check` should report `No broken requirements found`. Installation can take a
few minutes the first time. This uses the environment activated in step 2; it does
not create a separate venv. Windows CPU is the validated platform.

### 6. Register the Jupyter kernel

```sh
python -m ipykernel install --sys-prefix --name ppg-workshop-showcase --display-name "PPG Workshop Showcase"
```

This makes Jupyter use the environment containing the installed framework.

### 7. Open and run a notebook

For the full workshop:

```sh
jupyter lab workshop.ipynb
```

For the shorter two-fold CPU workshop:

```sh
jupyter lab workshop_cpu_short.ipynb
```

In Jupyter, select **PPG Workshop Showcase** as the kernel, then run cells from top
to bottom using **Shift+Enter**. If the wrong kernel is selected, use
**Kernel -> Change Kernel**. The first executable cell creates local workspace folders.

Run the download cells before the live session. DaLiA is about 2.7 GB compressed,
and initial download/extraction is separate from training time. The full notebook's
default teaching profile passed on the instructor PC in about 57 seconds **with
assets already downloaded**; that is not a promise for every machine or the full-data profile.

To view results immediately without running code, open
[the executed full notebook](examples/workshop_with_outputs.ipynb). Use the clean
notebooks at the repository root for your own run.

### 8. Come back later

You do not need to reinstall or recreate the environment each time. In a new conda
terminal, activate it, enter your existing clone and launch Jupyter:

```sh
conda activate ppg_workshop_showcase
cd path/to/ppg-workshop
jupyter lab workshop.ipynb
```

Replace `path/to/ppg-workshop` with the folder you cloned in step 4. Keep Jupyter's
terminal open while working; stop the server with **Ctrl+C** when finished.

## Install with pip (private access)

Participants need access to [the private installer repository](https://github.com/mamerm/ppg-workshop-runtime)
and must authenticate Git with their own GitHub account. The original framework
repository is not needed. There is no manual wheel or ZIP download.

With conda installed, run:

```sh
conda create -n ppg_workshop_showcase --override-channels -c conda-forge python=3.11 pip git -y
conda activate ppg_workshop_showcase
python -m pip install "ppg-experiment-framework[workshop] @ git+https://github.com/mamerm/ppg-workshop-runtime.git@v0.1.3"
ppg-workshop init ./my-ppg-workshop --tasks baseline exercise
cd my-ppg-workshop
python -m ipykernel install --sys-prefix --name ppg-workshop-showcase --display-name "PPG Workshop Showcase"
jupyter lab workshop_cpu_short.ipynb
```

Select **PPG Workshop Showcase** in Jupyter. Existing task/template files are
preserved. The generator does not download data or start training; those steps
are explicit notebook cells.

### Authentication

The instructor grants participants access to **mamerm/ppg-workshop-runtime**.
Authenticate Git before installation. Git Credential Manager (included in Git for
Windows) can open a GitHub sign-in dialog. If you use GitHub CLI, run
`gh auth login` followed by `gh auth setup-git`. You can verify access with:

```sh
git ls-remote https://github.com/mamerm/ppg-workshop-runtime.git
```

A 404 or "repository not found" usually means the account lacks access or Git
has not authenticated. Do not put access tokens into notebooks or environment YAML.

### Exact tested Windows CPU setup

If you already have this workshop folder, authenticate Git and run
`powershell -ExecutionPolicy Bypass -File .\setup.ps1` from a conda-enabled prompt.
The script creates the environment using conda-forge, installs pinned CPU
requirements and the framework directly through pip, checks dependencies and
registers the kernel. No wheel needs to be placed in `packages/`.

Alternatively, from this folder run `conda env create -f environment.windows-cpu.yml`.
Use `environment.yml` on other platforms (not execution-tested here). Some Miniconda
installations inspect unused Anaconda channels through a terms plugin; the setup
script uses explicit conda-forge channels and avoids that issue.

After generating a workspace with the simple pip command, Windows participants
can apply the exact dependency snapshot with
`python -m pip install -r requirements-tested-windows-cpu.txt`.

See `INSTRUCTOR.md` for the agenda and `COVERAGE.md` for the API tour. Export an
activated environment with `python export_environment.py`. The export uses the
private pip URL instead of a local wheel path. Recreating it requires Git and access
to the same installer repository.

The library's `create_workspace` API remains available for Python scripts. Set
`PPG_WORKSPACE` before importing processing/training modules when running outside
the workspace; the notebook handles this automatically.

## Before the live session

Execute the download cells beforehand. DaLiA is approximately 2.7 GB compressed;
reserve at least 15 GB for the environment, extraction, intermediates and results.
PaPaGei-S is approximately 23 MB. Download/extraction are cached. The complete
download is required even in quick mode. Interrupted downloads retain `.part`
files; rerunning restarts them and only completed files receive the final name.

If an instructor provides an existing `dalia_data.zip`, place it under
`data/downloads/`. The weights are verified against the checksum published on
Zenodo. URLs and checksums are configurable in `configs/workshop.yaml`.

## Notebook and tasks

`workshop.ipynb` includes a fully worked example and a runnable reference solution
for changing MLP dropout. Ask participants to predict the effect and make the
change before revealing that cell. `tasks/baseline/` and `tasks/exercise/` provide
folders for their own configs, figures and results.

Quick mode uses six subjects, the first 600 seconds per subject, three outer
folds, and a short epoch budget. It demonstrates execution, not benchmark-quality
performance. `PPG_WORKSHOP_MODE=full` uses all subjects and complete recordings;
runtime and memory use increase substantially. Mode and settings are visible in
the notebook. The exercise changes one model setting and reuses the saved splits.

Figures include raw BVP and labels, subject coverage, waveforms and derivatives,
split membership, prediction agreement, error versus prediction/reference,
model/subject error violins, subject MAE, signed/absolute error versus mean
absolute first/second derivatives, and high-error waveforms. Outputs are PDF and
PNG. Tables retain original sample indices for auditable feature joins.

Training uses the library's formatter, DataProcessor, experiment-ready I/O,
split artifacts, static orchestrator and TorchTrainingBackend. There is no
separate notebook training loop. The runner saves exact configurations and
held-out predictions. The summary includes package versions and experiment settings.

Sections 16-21 extend the tour with disk/RAM HDF5 reads, torch loaders, a custom
transform, filtering, fitted normalization, window sequences, persisted sample/batch
transforms, alternate group splits, and Integrated Gradients with convergence plots.

## Interpretation

Positive error means prediction minus reference heart rate. Derivative features
are computed from unnormalized processed BVP using seconds as the time unit.
Window-level violin plots are descriptive: overlapping windows are not independent
subjects. Report per-subject metrics as well as pooled scores. Fit preprocessing
using training subjects only and use validation subjects for model selection.
Do not repeatedly tune against the displayed test results.

## Private distribution

This public repository contains notebook/configuration files. The separate private
[installer repository](https://github.com/mamerm/ppg-workshop-runtime) contains the built wheel and a small pip build adapter; it has
no framework development history, datasets or experiments. Participants install
using their own GitHub credentials. Nothing is published to PyPI.

The current runtime package contains CPython 3.11 bytecode instead of readable
framework `.py` files. Notebook examples and setup scripts remain readable.
Bytecode can still be disassembled or reverse engineered; this is a deterrent to
casual inspection, not confidentiality protection. CPython 3.11 is required. Access revocation
prevents new authenticated downloads but does not remove previously installed copies.
The public teaching repository has a fresh history and no source-containing ZIP
releases. The runtime repository must remain private. Older instructor repositories
and their source-containing ZIP releases are not required by participants.

## Sources

- PPG-DaLiA: Reiss, Indlekofer and Schmidt (2019), UCI Machine Learning Repository,
  https://doi.org/10.24432/C53890 (CC BY 4.0).
- Dataset timing and format: https://archive.ics.uci.edu/ml/machine-learning-databases/00495/readme.pdf
- PaPaGei: https://github.com/Nokia-Bell-Labs/papagei-foundation-model
- PaPaGei weights: https://doi.org/10.5281/zenodo.13983110

Consult upstream notices when redistributing data or weights. They are downloaded
separately and are not embedded in the wheel or public template.

## Short workshop preview

Validated on Windows CPU in about 59 seconds with data already downloaded. This
includes the worked grid, participant grid, frozen PaPaGei comparison and IG.

![Live learning curves](preview/cpu_short_learning_curves.png)

![Selected-window Integrated Gradients](preview/cpu_short_window_ig.png)

## Full notebook with saved outputs

[View the executed full workshop](examples/workshop_with_outputs.ipynb), including
all plots, model comparisons, the advanced API tour and Integrated Gradients.
All 26 executable cells passed in **56.7 seconds on CPU** on 8 October 2026
using the default quick profile and cached downloads. Run the clean
`workshop.ipynb` at the repository root for your own experiment.
