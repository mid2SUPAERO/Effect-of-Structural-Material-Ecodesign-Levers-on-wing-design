## ✈️ `rp_OAS` — OpenAeroStruct Simulations

This folder contains simulations and analyses using **OpenAeroStruct (OAS)** to evaluate the impact of structural material choices on aircraft wing performance.

### 📌 Purpose

To assess how different materials affect:

* Wingbox structural mass
* Fuel consumption
* Environmental performance

### 🛠️ Methodology

* **Aircraft Models**: Airbus A320-200 / A321-200
* **Wing Geometry**: Based on CeRAS specifications
* **Tool Used**: [OpenAeroStruct](https://github.com/mdolab/OpenAeroStruct)
* **Optimization Goal**: Minimize fuel burn while meeting structural constraints

### 🧪 Materials Studied

* Aluminum 6061
* CFRP (Carbon Fiber Reinforced Polymer)
* Steel
* Titanium

### 📂 Folder Contents

#### Python Scripts

* `A320_AL6061_test.py`, `A321_CFRP_test.py`, etc.

  * Each script runs a structural/material optimization for a specific configuration.

#### Excel Files (`.xlsx`)

* Serve **dual purpose**:

  1. **Input Sheets**:

     * Aircraft properties (mass, range, etc.)
     * Wing geometry
     * Flight profile parameters
  2. **Results Sheets**:

     * Outputs like wingbox mass, fuel burn, and stress/strain metrics
