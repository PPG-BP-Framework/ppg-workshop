# Validation

The full notebook passed all 26 executable cells in 56.7 seconds on an AMD Ryzen 7
3700X CPU with cached downloads. The short notebook passed all 16 code cells in
58.9 seconds, including live learning curves, two-fold grid searches and window IG.
The long profile uses six subjects x ten minutes; the short uses six x two minutes.
These measurements exclude initial downloads and do not establish benchmark accuracy.

Nine focused tests passed, including train-only normalization, derivative units,
sample identity joins, scaffold preservation, download integrity and live logger
cleanup. Both notebooks ran using compiled framework modules on CPython 3.11.17.

Version 0.1.4 updates distribution and setup resources to the single public repository:
https://github.com/PPG-BP-Framework/ppg-workshop
Model and processing code is unchanged from the tested bytecode runtime. The build
adapter verifies the artifact checksum. The environment files and generated workshop
resources all reference the public installation URL. No login is required.

The runtime has no readable framework .py modules; notebook examples and setup scripts
remain readable. Bytecode is not a security boundary and can be reverse engineered.
Windows CPU was validated; other operating systems and Python minor versions were not.
Use Python 3.11. Public distribution does not include raw data or pretrained weights.
