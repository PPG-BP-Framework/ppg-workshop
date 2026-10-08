# PPG workshop: clone, install and run

**Everything needed to install is in this public repository:** both notebooks,
configs, task templates, environment files and the compiled framework wheel in
`artifacts/`. No private repository, invitation, GitHub login or token is required.
The notebook downloads DaLiA and PaPaGei weights separately.

## Step-by-step CPU setup

The existing `ppg_workshop_showcase` environment, `setup.ps1` and
`environment.windows-cpu.yml` use CPU PyTorch. Keep using them for CPU runs.
For an NVIDIA GPU, use the separate [GPU setup](#nvidia-gpu-setup-windows) below.

### 1. Open a conda terminal

Use Miniconda Prompt or Anaconda Prompt on Windows, or a terminal with conda
initialized on macOS/Linux. Install Miniconda first if needed.

```sh
conda --version
```

### 2. Create and activate the environment

**Pip does not create an environment.** Conda creates it and activation selects it.
CPython **3.11** is required by the compiled runtime. If the environment already
exists, skip creation and just activate it.

```sh
conda create -n ppg_workshop_showcase --override-channels -c conda-forge python=3.11 pip git -y
conda activate ppg_workshop_showcase
python --version
```

### 3. Clone this public repository

```sh
git clone https://github.com/PPG-BP-Framework/ppg-workshop.git
cd ppg-workshop
```

If you already have a clone, enter its folder and run `git pull` instead.
The notebooks and configs are already here; no scaffold-generation step is needed.

### 4. Install from this folder

For the exact tested **Windows CPU** dependency versions, run this first.
Skip this platform-specific snapshot on macOS/Linux.

```sh
python -m pip install -r requirements-tested-windows-cpu.txt
```

Then install the included framework and notebook dependencies:

```sh
python -m pip install ".[workshop]"
python -m pip check
```

Pip installs into the active conda environment. `pip check` should report
`No broken requirements found`. The first installation may take several minutes.
Windows CPU is the validated platform; macOS/Linux have not been execution-tested.

### 5. Register the kernel

```sh
python -m ipykernel install --sys-prefix --name ppg-workshop-showcase --display-name "PPG Workshop Showcase"
```

### 6. Open either notebook

```sh
jupyter lab workshop.ipynb
```

Or use the shorter live-session version:

```sh
jupyter lab workshop_cpu_short.ipynb
```

Select **PPG Workshop Showcase** in Jupyter (Kernel -> Change Kernel if necessary),
then run cells from top to bottom with **Shift+Enter**. The first executable cell
creates missing data/output folders. Download cells should be run before class:
DaLiA is about **2.7 GB compressed**; reserve roughly **15 GB** for setup and artifacts.
The shorter profile reduces training work, not the original archive size.

### 7. Return later

```sh
conda activate ppg_workshop_showcase
cd path/to/ppg-workshop
jupyter lab workshop.ipynb
```

Replace the path with your actual clone. Keep the terminal open while using Jupyter;
stop its server with Ctrl+C afterwards. There is no need to recreate the environment.

## NVIDIA GPU setup (Windows)

Use a separate **`ppg_workshop_gpu`** environment for the full `workshop.ipynb`.
The existing CPU environment and notebooks stay unchanged. You need an NVIDIA
GPU and a driver compatible with CUDA 12.8; check that `nvidia-smi` recognizes it.
This uses the [official PyTorch 2.8 CUDA 12.8 wheel](https://pytorch.org/get-started/previous-versions/#v280).

From a conda-enabled terminal, inside your cloned `ppg-workshop` folder:

```sh
conda create -n ppg_workshop_gpu --override-channels -c conda-forge python=3.11.17 pip git -y
conda activate ppg_workshop_gpu
python -m pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu128
python -m pip install ".[workshop]"
python -m pip check
python -c "import torch; assert torch.cuda.is_available(), 'CUDA unavailable'; print(torch.__version__, torch.cuda.get_device_name(0)); print(torch.ones(1, device='cuda').cpu())"
python -m ipykernel install --sys-prefix --name ppg-workshop-gpu --display-name "PPG Workshop GPU"
```

Do not install `requirements-tested-windows-cpu.txt` or run `setup.ps1` in this
GPU environment: those select CPU PyTorch. The matching environment definition
is [environment.windows-gpu.yml](environment.windows-gpu.yml), which can also be
created with `conda env create -f environment.windows-gpu.yml`; then activate it,
run the checks above and register its kernel.

Before starting Jupyter, select CUDA using the full notebook's existing setting.
In **PowerShell**:

```powershell
conda activate ppg_workshop_gpu
$env:PPG_WORKSHOP_DEVICE = "cuda"
jupyter lab workshop.ipynb
```

In **Anaconda/Miniconda Prompt (cmd)** instead:

```bat
conda activate ppg_workshop_gpu
set PPG_WORKSHOP_DEVICE=cuda
jupyter lab workshop.ipynb
```

Select **PPG Workshop GPU** in Jupyter (Kernel -> Change Kernel). Start Jupyter
from this terminal so its kernel inherits the setting, and set it again whenever
you open a new terminal. Without it, the full notebook defaults to CPU even if
CUDA PyTorch is installed. For later GPU sessions, only activation, the device
setting and the Jupyter command are needed.

**`workshop_cpu_short.ipynb` explicitly selects CPU.** It stays a CPU example even
when opened with the GPU kernel. For CPU sessions, use the CPU setup above and
clear `PPG_WORKSHOP_DEVICE` if reusing the same terminal (`Remove-Item
Env:PPG_WORKSHOP_DEVICE -ErrorAction SilentlyContinue` in PowerShell, or
`set PPG_WORKSHOP_DEVICE=` in cmd).

## Install directly with pip without cloning manually

After creating and activating a Python 3.11 conda environment with Git:

```sh
python -m pip install "ppg-experiment-framework[workshop] @ git+https://github.com/PPG-BP-Framework/ppg-workshop.git@v0.1.4"
ppg-workshop init ./my-workshop
cd my-workshop
python -m ipykernel install --sys-prefix --name ppg-workshop-showcase --display-name "PPG Workshop Showcase"
jupyter lab workshop_cpu_short.ipynb
```

Both notebooks and their configs are included in the installed package. The init
command creates them without overwriting existing participant edits. Authentication
is not needed for this installation route either.

## Alternative Windows setup and environment export

From a clone in a conda-enabled prompt, `powershell -ExecutionPolicy Bypass -File .\setup.ps1`
creates the environment, installs pinned CPU packages and the public runtime,
checks dependencies and registers the kernel. Use this instead of the manual setup.

`environment.windows-cpu.yml` recreates the tested Windows dependency choices;
`environment.yml` is the portable starting point. Both install from this public
repository. Run `python export_environment.py` inside an activated environment to
write `environment.exported.yml` without machine-specific installation paths.

## Notebook content

- `workshop_cpu_short.ipynb`: two subject folds, five epochs per candidate, live
  learning curves, worked and editable participant grid searches, optional frozen
  PaPaGei, error/violin/derivative plots and Integrated Gradients on a selected window.
- `workshop.ipynb`: complete workflow and extended API tour, including streaming,
  transforms, window sequences, alternate splits and attribution.
- [Executed full notebook](examples/workshop_with_outputs.ipynb): all plots and outputs
  already visible. The default teaching profile passed all 26 executable cells in
  **56.7 seconds on CPU** with assets cached. The short notebook passed in about
  **59 seconds**, including live plots and grid searches. Full-data/GPU runtime is not measured.

See `INSTRUCTOR.md` for the agenda, `COVERAGE.md` for the API tour and `VALIDATION.md`
for checks. Quick-profile metrics demonstrate the workflow, not benchmark performance.

## Runtime distribution

The public wheel contains CPython 3.11 bytecode instead of readable framework `.py`
modules. This discourages casual inspection but does not prevent disassembly,
reverse engineering or copying. Notebook examples and setup scripts remain readable.
The checksum in `distribution.json` is verified by the pip build adapter.

## Data and model sources

- PPG-DaLiA: Reiss, Indlekofer and Schmidt (2019), UCI, https://doi.org/10.24432/C53890 (CC BY 4.0).
- Dataset format: https://archive.ics.uci.edu/ml/machine-learning-databases/00495/readme.pdf
- PaPaGei implementation: https://github.com/Nokia-Bell-Labs/papagei-foundation-model
- PaPaGei weights: https://doi.org/10.5281/zenodo.13983110

Data and weights are fetched separately. Preserve their upstream notices.
