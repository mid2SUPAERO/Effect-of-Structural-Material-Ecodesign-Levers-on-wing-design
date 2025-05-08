# CatalogsVAE - Extended for Multi-Objective Material Composition Optimization

This repository builds upon the original [CatalogsVAE](https://github.com/UW-ERSL/CatalogsVAE) project by extending its scope to include **multi-objective optimization of new material compositions**. 

Our goal is to explore the continuous space of synthesized materials using **Variational Autoencoders (VAEs)**, and optimize for properties such as **cost, energy consumption, material waste**, and **effective density** — under realistic material blending constraints.

## 📄 Project Highlights

- **Trained VAE on real engineering material data**
- **Synthetic dataset** of 5000 valid material blends generated using domain constraints
- **Feature extraction**: `cost`, `energy`, `waste`, `rho_eff`
- **Latent space embedding** of new materials for intuitive visualization and optimization
- **Optimization-ready latent space** for future multi-objective search (e.g., NSGA-II)

## 📁 Structure

- `src/`  
  Core VAE model code, encoders/decoders, utility functions.
  
- `data/`  
  Original material datasets and constraint data.
  
- `latentSpace_ourRP.ipynb`  
  End-to-end notebook to train the VAE and embed materials into latent space.

- `computed_material_features_to_use.xlsx`  
  Your synthetic material compositions with derived properties and dominant material family.

## 📦 Dependencies

- `numpy`
- `pandas`
- `torch` (PyTorch)
- `matplotlib`
- `scipy`
- `seaborn`
- `openpyxl` (for Excel I/O)

You can install them via:

```bash
pip install numpy pandas torch matplotlib scipy seaborn openpyxl

