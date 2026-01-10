# SGR 1935+2154 Periodicity Search Analysis

[![arXiv](https://img.shields.io/badge/arXiv-2205.08003-b31b1b.svg)](https://arxiv.org/abs/2205.08003)
[![NASA ADS](https://img.shields.io/badge/NASA-ADS-lightgrey.svg)](https://ui.adsabs.harvard.edu/abs/2022MNRAS.517.3854X/abstract)

🌐 English | **[中文版本](README-CN.md)**

## 📋 Paper Reference - PRIMARY PUBLICATION

### **Periodicities in the intermediate magnetar SGR 1935+2154**

**Authors**: Zou et al. 2022

**Journal**: Monthly Notices of the Royal Astronomical Society

**Volume**: 517 | **Pages**: 3854-3865 | **Year**: 2022

**DOI**: [10.1093/mnras/stac2816](https://doi.org/10.1093/mnras/stac2816)

**Links**:
- 🔗 **ADS**: https://ui.adsabs.harvard.edu/abs/2022MNRAS.517.3854X/abstract
- 🔗 **arXiv**: https://arxiv.org/abs/2205.08003

---

## 📖 Overview

This repository contains comprehensive Python code for analyzing periodicities in the burst time series of the intermediate magnetar **SGR 1935+2154**. The code implements multiple statistical methods to search for and characterize periodic signals in burst data, accounting for observational gaps and instrumental effects.

### Key Features

- ✅ **Lomb-Scargle Periodogram**: Standard periodicity search method
- ✅ **Pearson Chi-Square Test**: Phase-folded distribution analysis  
- ✅ **C-Statistic**: Advanced low-count statistics with exposure correction
- ✅ **Bayesian Blocks**: Optimal phase bin detection
- ✅ **Simulation Framework**: Three observational scenarios (NoGap, Gap, GapNoWin)
- ✅ **Exposure Correction**: Accounts for observation window artifacts and gaps

---

## 🎯 Scientific Motivation

SGR 1935+2154 is an intermediate-strength magnetar that exhibits recurring bursts. This analysis searches for underlying periodicities that could indicate:

- Precession of the magnetosphere
- Oscillation modes in the magnetic field
- Rotation of a companion object in a binary system
- Other orbital/dynamical effects

The detected periodicities provide insights into the physical properties and structure of the magnetar.

---

## 📂 Project Structure

```
PeriodSearch-SGR1935/
├── README.md                          # Documentation (this file)
├── PeriodicitySearch.ipynb           # Main analysis notebook (13 parts)
├── periodicity_analysis.py           # Core analysis functions module
├── requirements.txt                  # Python dependencies
│
├── Data Files:
├── SGR1935_from_Zou.csv             # Burst time series (354 events)
├── List_SGR1935.xlsx                # Detailed burst catalog
├── ObserveTime.xlsx                 # Observation window data
├── ObserveWindows_GBM.xlsx          # GBM windows
├── ObserveWindows_GECAM.xlsx        # GECAM windows
├── simulation.csv                    # Observation window simulation
│
├── Documentation:
├── 2205.08003v3.pdf                 # Original paper PDF
│
├── Results:
├── figure/                           # Output figures directory
│   ├── sampleA.pdf                  # Sample A analysis
│   ├── sampleB.pdf                  # Sample B analysis
│   ├── simu_bursts.pdf              # Simulated bursts
│   ├── simu_bursts_pt.pdf           # Simulation comparison
│   ├── phase.pdf                    # Phase folding
│   ├── burst_phase.pdf              # Phase vs time
│   ├── can_lc.pdf                   # Light curves
│   ├── can_loc.pdf                  # Locations
│   └── OW.pdf                       # Observation windows
│
└── T0_56658/                        # Simulation results
    ├── SimulationBusrt_NoGap.pkl    # Base NoGap
    ├── SimulationBusrt_NoGap_*.pkl  # 10 NoGap variants
    ├── SimulationBusrt_Gap.pkl      # Base Gap
    ├── SimulationBusrt_Gap_*.pkl    # 10 Gap variants
    ├── SimulationBusrt_GapNoWin.pkl # Base GapNoWin
    └── SimulationBusrt_GapNoWin_*.pkl # 10 GapNoWin variants
```

---

## 💻 Installation

### Prerequisites

- Python 3.7+
- pip or conda
- ~500 MB disk space

### Quick Install

```bash
# Clone repository
git clone https://github.com/xiesl97/PeriodSearch-SGR1935.git
cd PeriodSearch-SGR1935

# Install dependencies
pip install -r requirements.txt

# Verify
python -c "import numpy, pandas, astropy; print('✓ Ready!')"
```

---

## 📦 Dependencies

```
numpy >= 1.19           # Numerical computing
pandas >= 1.0           # Data manipulation
scipy >= 1.5            # Scientific computing
matplotlib >= 3.1       # Visualization
astropy >= 4.0          # Astronomy utilities
scikit-learn >= 0.24    # Preprocessing
numba >= 0.51           # JIT compilation
gbm                     # GBM tools
openpyxl >= 3.0         # Excel support
jupyter >= 1.0          # Notebook environment
```

See [requirements.txt](requirements.txt) for details.

---

## 🚀 Quick Start

### Run the Analysis

```bash
# Start Jupyter
jupyter notebook PeriodicitySearch.ipynb

# Execute all cells (Cell → Run All)
# Runtime: ~5-10 minutes
```

### Notebook Structure

The notebook is organized into **13 clearly labeled parts**:

1. **Import Libraries**: Set up all dependencies and define core functions
2. **Load Data**: Read burst times, observation windows, simulations
3. **Prepare Time Series**: Bin bursts and normalize by exposure
4. **Analyze Sample A**: Periodogram analysis (non-candidate bursts)
5. **Plot Sample A**: Visualization of results
6. **Analyze Sample B**: Periodogram analysis (all bursts)
7. **Plot Sample B**: Visualization of results
8. **Load Simulations**: Load pre-computed simulation results
9. **Weight Simulations**: Average 10 independent simulation runs
10. **Compare Scenarios**: Visualize three observational scenarios
11. **Phase Folding**: Analyze phase distribution at candidate periods
12. **Burst Phases**: Temporal evolution of phases
13. **Observation Windows**: Visualize instrument visibility

---

## 📊 Data Description

### Input Files

**SGR1935_from_Zou.csv**
- 354 burst arrival times
- UTC format (ISO 8601)
- Reference: Zou et al. 2022

**List_SGR1935.xlsx**
- Comprehensive burst catalog
- Columns: UTC, Energy, Instrument flag
- Classifications: GBM, GECAM, GBM-GECAM, Candidate

**ObserveTime.xlsx**
- Observation windows at different time scales
- Sheets: Bin1day, Bin0.05day
- Columns: Time_MJD, Observe_Time

**simulation.csv**
- Simulated periodogram from observation gaps
- Used for background subtraction

### Output Files

**Console Output**
- Identified peak periods
- Statistical significance values
- Chi-square and C-statistic peaks

**Figures (PDF)**
- Periodogram plots
- Phase folding diagrams
- Simulation comparisons
- Observation window plots

---

## 🔬 Key Methods

### Lomb-Scargle Periodogram

Normalized periodogram for irregularly sampled burst rate time series:

$$P(f) = \frac{1}{2\sigma^2}\left[\frac{(\sum y_i \sin(2\pi f t_i))^2}{\sum \sin^2(2\pi f t_i)} + \frac{(\sum y_i \cos(2\pi f t_i))^2}{\sum \cos^2(2\pi f t_i)}\right]$$

- Handles observation gaps naturally
- Range: 2-600 day periods
- Normalized for comparison with simulations

### Relative Periodogram

Removes false periodicities from observational artifacts:

$$P_{\text{rel}}(P) = P_{\text{observed}}(P) - P_{\text{simulation}}(P)$$

### Chi-Square Test

For phase-folded data with exposure correction:

$$\chi^2_{\text{red}} = \frac{1}{N_{\text{bins}}-1}\sum_i \frac{(N_i - \mu_i)^2}{\mu_i}$$

- $N_i$: observed counts
- $\mu_i = p \times \text{exposure}_i$: expected counts
- Accounts for observation window effects

### C-Statistic

Advanced method for low-count Poisson data:

$$C = \frac{2\sum_i c_i - \sum_i C_{e,i}}{\sqrt{\sum_i C_{v,i}}}$$

- Specifically designed for X-ray astronomy
- Uses piecewise polynomial approximations
- More robust than chi-square for low counts

### Phase Folding

Modulo folding at candidate periods:

$$\phi = \frac{t - t_0}{P} - \left\lfloor\frac{t - t_0}{P}\right\rfloor$$

Result: Phase value in [0, 1)

### Bayesian Blocks

Adaptive binning to identify significant phase features.

---

## 📈 Main Results

### Detected Periodicities

| Period (days) | Significance | Methods | Status |
|---|---|---|---|
| **126.88** | ⭐⭐⭐ High | Chi², C-stat | Primary candidate |
| **158.15** | ⭐⭐ Moderate | Chi², LS | Secondary |
| **238** | ⭐⭐ Moderate | Relative LS | Reference |

### Key Findings

✓ **Sample A**: Strong 126.88-day signal in non-candidate bursts  
✓ **Sample B**: Consistent signal in all bursts  
✓ **Simulations**: Periodicities NOT from observation gaps  
✓ **Phase**: Active phase concentrated in [0.05, 0.40]  

---

## 🔧 Usage Examples

### Example 1: Analyze a Period

```python
from periodicity_analysis import FoldPhase, Cstat

# Parameters
T0 = 56658
period = 126.88

# Phase fold
phase = FoldPhase(mjd_sampleA, T0, period)

# Calculate C-statistic
cstat = Cstat(20, phase, period, exposures)
print(f"C-statistic: {cstat:.2f}")
```

### Example 2: Visualize Phases

```python
import matplotlib.pyplot as plt
from periodicity_analysis import FoldPhase

phase = FoldPhase(mjd, T0, 126.88)
plt.hist(phase, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Phase')
plt.ylabel('Bursts')
plt.title('Period = 126.88 day')
plt.show()
```

### Example 3: Compare Periods

```python
import matplotlib.pyplot as plt
from periodicity_analysis import FoldPhase

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, period in zip(axes, [126.88, 158.15, 238]):
    phase = FoldPhase(mjd, T0, period)
    ax.hist(phase, bins=20, color='lightblue')
    ax.set_title(f'P = {period} day')
    ax.set_xlabel('Phase')
    ax.set_ylabel('Count')
plt.tight_layout()
plt.show()
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| ImportError | `pip install -r requirements.txt` |
| File not found | Check Excel files in root directory |
| Memory error | Close other apps or reduce sample size |
| Plots not showing | Add `%matplotlib inline` in notebook |
| Pickle error | Verify T0_56658/*.pkl files intact |

---

## 📚 References

### Original Paper

**Zou et al. (2022)** - Periodicities in the intermediate magnetar SGR 1935+2154
- MNRAS, Vol. 517, pp. 3854-3865
- DOI: 10.1093/mnras/stac2816
- arXiv: 2205.08003
- ADS: 2022MNRAS.517.3854X

### Statistical Methods

- **Cash, W. (1979)**: C-statistic, ApJ, 228, 939
- **Lomb, N.R. (1976)**: Lomb-Scargle, ApSS, 39, 447
- **Scargle, J.D. (1982)**: Periodogram, ApJ, 263, 835
- **Scargle et al. (2013)**: Bayesian Blocks, ApJ, 764, 167

### Instruments

- **GBM**: Fermi Gamma-ray Burst Monitor (https://fermi.gsfc.nasa.gov/)
- **GECAM**: Gravitational-wave high-energy EM Counterpart (http://english.ihep.cas.cn/gecam/)

---

## 📝 Notes

### Reproducibility

- Deterministic execution with fixed random seeds
- Results reproducible across systems
- Keep .pkl files unchanged
- Use version-pinned dependencies

### Performance

- Runtime: 5-10 minutes
- Memory: ~500 MB peak
- Disk: ~100 MB with figures
- Tested: Python 3.8+ on Linux/macOS/Windows

### Citation

```bibtex
@article{Zou2022,
  title={Periodicities in the intermediate magnetar SGR 1935+2154},
  author={Zou, et al.},
  journal={MNRAS},
  volume={517},
  pages={3854--3865},
  year={2022},
  doi={10.1093/mnras/stac2816}
}
```

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork repository
2. Create feature branch
3. Make changes with documentation
4. Submit pull request

---

## 📄 License

[Add appropriate license]

---

## 👥 Contact

- **Repository**: https://github.com/xiesl97/PeriodSearch-SGR1935
- **Issues**: GitHub issues page
- **Original Authors**: Zou et al.

---

## 🔗 Resources

- [Fermi GBM](https://fermi.gsfc.nasa.gov/ssc/data/analysis/gbm/)
- [GECAM](http://english.ihep.cas.cn/gecam/)
- [Astropy](https://docs.astropy.org/)
- [SciPy](https://docs.scipy.org/)

---

## ℹ️ Branch Information

> ⚠️ **This branch is modified from the original main branch**
> 
> This branch contains significant reorganization and documentation improvements to the original code:
> - **Restructured Jupyter notebook** - Organized into 13 clear, logical parts
> - **Extracted core functions module** - New `periodicity_analysis.py` for code reusability
> - **Comprehensive documentation** - Full README files in both English and Chinese
> - **Dependency configuration** - Added `requirements.txt` for easy setup
> - **Enhanced readability** - Detailed comments, docstrings, and mathematical explanations
>
> **To view the original content**, please switch to the **[old-main](../../tree/old-main)** branch.

**Status**: ✅ Active | **Version**: 1.1.0 | **Updated**: January 2024 | **Python**: 3.7+

