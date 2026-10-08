# Framework coverage

All examples call the installed package; no source checkout or `sys.path` patch is required.

| Area | Running example |
|---|---|
| Task scaffolding | `create_workspace`, CLI `ppg-workshop init` |
| Dataset download and formatting | UCI DaLiA download, aligned wrist BVP/HR, configurable subject/time subset |
| Foundation weights | Official PaPaGei-S download and published checksum |
| DataProcessor | Resampling, aligned windows, missing-target removal, HDF5 export |
| Data inspection | Raw waveforms, label coverage, metadata, sample identities |
| Splits and fitted preprocessing | Saved three-way subject membership, train-only fitted z-normalization |
| Torch model construction | MLP config and frozen PaPaGei + trainable head; parameter counts |
| Experiment orchestration | Config dry run, saved artifacts, seeded training, validation, early stopping |
| Torch training backend | Used by the orchestrator for every model and fold; no notebook training loop |
| Evaluation | MAE, RMSE, R2, Pearson r, bias, pooled and per-subject tables |
| Visual diagnostics | Agreement, signed errors, violins, derivative/error relationships, high-error inputs |
| Participant exercise | Dropout change with fixed data/splits and a runnable reference solution |
| Streaming and loaders | Record HDF5 disk/RAM batches and framework torch DataLoader |
| Transform extension | Custom `BaseTransform`, moving-average filter, imputation, fit/apply normalization |
| Temporal inputs | Window-sequence export and shape inspection |
| Persisted transformations | Sample-wise and batched experiment-ready transformations |
| Alternative evaluation splits | Single holdout, grouped k-fold, leave-one-subject-out |
| Explainability | Checkpoint-based Integrated Gradients, saved-prediction verification, convergence/importance plots |
| Reproducibility | Configs, split artifacts, checkpoints, tables, manifest, conda definitions and export script |

The tour demonstrates the active reusable workflow, not every dataset adapter,
filter preset or network architecture. Other dataset/model integrations need their
own data, weights and dependencies. Legacy/non-torch backend skeletons are not
advertised as runnable. Fixed-grid event classification is a separate task from
this DaLiA regression workshop. Full-dataset and GPU execution are configurable
but have not been validated by this workshop's CPU smoke run.
