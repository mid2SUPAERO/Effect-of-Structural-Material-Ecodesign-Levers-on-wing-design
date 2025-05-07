import numpy as np
import pandas as pd

# Parameters
materials = ['Aluminium', 'Steel', 'Titanium', 'CFRP']
BtF = np.array([5, 6, 10, 1.5])                  # Buy-to-Fly ratios
densities = np.array([2780, 7800, 4430, 1600])   # kg/m^3
energies = np.array([163, 20, 536, 514])         # MJ/kg
costs = np.array([2.5, 2.4, 21, 90])             # $/kg
nr_frac = np.array([0.05, 0.05, 0.15, 1.0])       # Non-recyclable fractions
min_wt_frac = np.array([0.15, 0.01, 0.01, 0.01])  # Minimum weight fraction constraints


def compute_features(w):
    w_full = np.append(w, 1.0 - np.sum(w))
    v = (w_full / densities) / np.sum(w_full / densities)
    cost = np.sum(w_full * costs * BtF)
    energy = np.sum(w_full * energies * BtF)
    waste = np.sum(w_full * (BtF - 1) * nr_frac)
    rho_eff = np.sum(v * densities)
    return {
        'w_Al': w_full[0],
        'w_Steel': w_full[1],
        'w_Titanium': w_full[2],
        'w_CFRP': w_full[3],
        'rho_eff': rho_eff,
        'cost': cost,
        'energy': energy,
        'waste': waste
    }

# Sampling feasible weight combinations
N = 5000
samples = []
ub = 1.0 - min_wt_frac[3]  # max sum of first three
while len(samples) < N:
    # random between minimum and ub
    w = min_wt_frac[:3] + np.random.rand(3) * (ub - min_wt_frac[:3])
    if w.sum() <= ub:
        w4 = 1.0 - np.sum(w)
        # Titanium constraint: w_Ti >= 0.25 * w_CFRP
        if w[2] >= 0.25 * w4:
            samples.append(compute_features(w))

# Create DataFrame
df_samples = pd.DataFrame(samples)

# Sort by ascending Aluminium weight to help visualize
df_samples = df_samples.sort_values(by='w_Al')

# Save to Excel
df_samples.to_excel("computed_material_features_sorted.xlsx", index=False)

# Determine the dominant material per sample
weight_columns = ['w_Al', 'w_Steel', 'w_Titanium', 'w_CFRP']
families = ['Aluminium', 'Steel', 'Titanium', 'CFRP']

# Find the index of the maximum weight in each row
max_indices = df_samples[weight_columns].values.argmax(axis=1)

# Assign the dominant family
df_samples['family'] = [families[idx] for idx in max_indices]

# Save as Excel
df_samples.to_excel("computed_material_features_to_use.xlsx", index=False)
