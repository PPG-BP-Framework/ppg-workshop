# Validation record

Validated on Windows CPU in a fresh conda environment, `ppg_workshop_showcase`.

- Python 3.11.17; torch 2.14.1+cpu; framework 0.1.1.
- Installed the wheel non-editably and installed the pinned Windows CPU requirements.
- `pip check`: no broken requirements.
- All 26 executable notebook cells passed, including MLP, frozen PaPaGei-S,
  the dropout exercise, advanced data APIs and checkpoint-based Integrated Gradients.
- Notebook execution: approximately 57 seconds with data/weights already cached.
- Six real DaLiA subjects, ten minutes each, 1,782 windows, three subject folds per model.
- 15 PDF and 18 PNG plots, plus metrics/prediction tables and checkpoints.
- Eight focused framework tests passed, including training-only normalization,
  derivative units and sample-identity joins, scaffold preservation and download integrity.
- Exported `environment.exported.yml` has no machine prefix or local installation URL.

The executed notebook is `workshop.executed.ipynb` (local, ignored by Git).
The download/extraction cache was reused; the notebook downloaded assets from the
published sources during preparation. Generated processing/training artifacts were
created in this standalone workspace. No framework source checkout is required.

## Distribution integrity

Wheel: `ppg_experiment_framework-0.1.1-py3-none-any.whl`

SHA256: `085f497ad0b82c6f00aa17813e0e800b84c37bd3dc6cf5201992692f443a729b`

The wheel is excluded from Git. The notebook, environment definitions, setup/export
scripts and teaching materials are tracked independently of the framework repo.

## Limits of this validation

This is a quick teaching run, not a full-data benchmark. Full profile, GPU,
macOS and Linux execution have not been tested here. The environment export and
requirements snapshot target Windows CPU; use `environment.yml` as the portable
starting point on other platforms. A 90-minute workshop assumes setup/downloads
are complete before the session.

## Authenticated pip update (0.1.2)

Successfully installed the private Git requirement from tag `v0.1.2` into the
workshop conda environment. Verified the installed distribution's Git provenance,
version, and site-packages import path. `pip check` passed. Generated and validated
the complete notebook and task structure without a manually downloaded wheel.
The installer backend preserves the original wheel bytes and rejects a modified
wheel whose digest differs from its manifest. The environment export now contains
the authenticated pip requirement and no local wheel path.

This update changes distribution/setup resources; model and processing code are
unchanged from the full v0.1.1 notebook run recorded above. The installer repository
is `https://github.com/mamerm/ppg-workshop-install` and remains private.

## CPU short workshop and bytecode runtime (0.1.3)

Validated the installed `cp311-none-any` runtime on Windows CPU with CPython 3.11.17.

- Short notebook: 16 executable cells passed in 58.9 seconds, with cached downloads.
- Full reference notebook: all 26 executable cells passed against the bytecode runtime.
- Short profile: six subjects, first 120 seconds each, 342 windows, two outer folds,
  five epochs per candidate. Two training subjects, one validation subject and three
  test subjects in each fold.
- Worked and participant grids: two candidates per fold. Verified the chosen candidate
  achieves the lowest recorded validation loss in each fold. The editable block can
  expand to four candidates; the teaching cap prevents accidental large sweeps.
- Live training/validation curves render during all three training blocks.
- Selected-window Integrated Gradients passed saved-prediction validation and produced
  waveform attribution, population and convergence plots. Window index is selected
  explicitly, independently of its error or attribution appearance.
- Nine focused tests passed, including log-handler cleanup when training fails.
- Authenticated pip installation from the new private runtime repository passed;
  `pip check`, both generated notebook templates and the environment export passed.

### Source visibility

The runtime wheel contains 99 compiled framework modules and no readable framework
`.py` implementations. `inspect.getsource(pipeline.run_task)` cannot retrieve source
from this installation. Editable notebook examples and setup/export scripts remain
readable. Bytecode can still be reverse engineered. This is a deterrent to casual
inspection, not protection of confidential implementation details.

The new private repository `mamerm/ppg-workshop-runtime` has no historical source
wheel. Older `ppg-workshop-install` tags and the teaching repository's ZIP release
still contain readable code and must remain instructor-only for this distribution.
No old repositories, tags or release assets were deleted.

Runtime wheel SHA256: `9d13461b657534032dc920e76ae91a46a0bf06c6b3e2fe38c398a844e88329cb`.
CPython 3.11 is required; other Python minor versions are unsupported. Windows CPU
was tested; other operating systems were not. Initial data downloads are excluded
from the recorded runtime, and quick-profile metrics are not benchmark-quality.
