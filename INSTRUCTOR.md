# Instructor guide

## Before participants arrive

1. Share https://github.com/PPG-BP-Framework/ppg-workshop and the public setup commands in README.md. No participant invitation or login is needed.
2. Ask participants to run the environment setup before the workshop. Use Windows CPU for the validated setup.
3. Run the notebook download cell in advance (approximately 2.7 GB archive plus extraction). The local prepared copy already has these cached.
4. Run `python execute_workshop.py --notebook workshop.ipynb --workspace . --output workshop.executed.ipynb --kernel ppg-workshop-showcase`.
5. Keep the executed notebook as a fallback for participants waiting for downloads. Restart the kernel before teaching and run cells in order.

## Short CPU route (recommended live)

Use `workshop_cpu_short.ipynb`. The defaults use six subjects, two minutes each,
two subject folds and five epochs per candidate. Complete the download beforehand.
Live learning curves update while candidates train. The participant grid settings
have their own cell directly above the run cell. Have participants change learning
rates first, then optionally add a second batch size (maximum four candidates).
Explain the instructor model's selected held-out window with Integrated Gradients
after the exercise. Point out the reference, prediction and convergence delta.

The compiled CPython 3.11 runtime is included in this public repository. Participants clone it and install with `python -m pip install ".[workshop]"`.

## Suggested 90-minute workshop

| Minutes | Activity | Sections |
|---|---|---|
| 0-10 | Question, data representation, signal and label timing | 1-3 |
| 10-25 | Processing, HDF5, leakage, subject splits | 4-6 |
| 25-40 | MLP baseline and frozen PaPaGei comparison | 7-8 |
| 40-55 | Errors, violins, subject metrics, derivatives | 9-11 |
| 55-70 | Participant changes dropout and compares under fixed splits | 12 |
| 70-80 | Trace predictions, save artifacts, discuss limitations | 13-15 |
| 80-90 | Pick an advanced demonstration and debrief | 16-21 |

The notebook includes more material than fits comfortably into 90 minutes.
Keep advanced sections as self-study or extend to a two-hour session. Setup and
data downloads are not part of the 90-minute teaching schedule.

## Participant exercise

Before revealing the reference solution in section 12, ask participants to:

- Copy the MLP configuration to `tasks/exercise/configs/`.
- Change only dropout from 0.2 to 0.4 and write a hypothesis.
- Reuse the same dataset, saved subject splits, normalization and epoch budget.
- Call `pipeline.run_task`, then compute pooled and per-subject metrics.
- Create a violin plot and identify a subject where performance changed.
- Explain why this one small comparison cannot establish a general improvement.

Alternative exercises: change hidden size, try L1 loss, or change head dropout on
frozen PaPaGei. Window length/filtering changes require fresh preprocessing and
new split/normalization artifacts, so reserve them for advanced participants.

## Files to distribute

The GitHub template contains teaching code, configs and environment definitions.
The artifacts/ directory in this public repository supplies the compiled library to pip without authentication.
The ignored data and weights are fetched by the notebook. Participants generate their notebook and tasks with `ppg-workshop init` after pip installation. No separate installer repository or ZIP bundle is needed.

## Teaching boundaries

This demonstrates heart-rate regression, not blood-pressure validation. Quick mode
uses six subjects and ten minutes each; performance is intentionally not presented
as a PaPaGei benchmark. Test plots are evaluation tools, not a repeated tuning target.
Attribution shows model sensitivity, not causality. A wheel does not hide Python
source from its recipients.
