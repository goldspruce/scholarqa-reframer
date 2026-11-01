# 🔬 ScholarQA Mechanistic Query Reframer

> **Transform leading, closed scientific hypotheses into open, multi-dimensional ScholarQA research inquiries.**  
> *A pedagogical scientific pre-processor that eliminates AI sycophancy, confirmation bias, and citation bluffing.*

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit App](https://img.shields.io/badge/Streamlit-UI-red.svg)](https://streamlit.io/)

---

## 1. Why This Tool Exists

In scientific research, **how you frame a question determines whether an AI discovers physical truth or hallucinates to confirm your bias.**

When a researcher feeds an AI a closed, leading hypothesis:
> *"Does solvent viscosity damp bacterial instantaneous thermal velocity according to Stokes' drag?"*

Frontier LLMs suffer from **sycophancy and anchor bias**:
1. The model's attention heads anchor on the suggested mechanism (*Stokes drag* and *viscosity*).
2. The model searches for reasons to agree with the user rather than checking first principles.
3. The retriever pulls irrelevant pages mentioning Stokes drag, and the LLM commits **Citation Bluffing** by misattributing the quote.

### The ScholarQA Solution
Following the **Allen Institute for AI (ScholarQA)** methodology, this tool acts as an intelligent pre-processor that:
1. **Decouples Invariants from Variables:** Separates equilibrium state functions from kinetic dissipation.
2. **Strips Confirmation Bias:** Replaces leading prompts with neutral, multi-dimensional mechanistic inquiries.
3. **Generates High-IDF Search Probes:** Produces targeted keyword sets that hit the exact physical derivations on disk.
4. **Educates the Researcher:** Provides a pedagogical critique explaining *why* the reframed formulation yields superior scientific evidence.

---

## 2. Reframing in Action (Example: Question 2)

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│ 1. YOUR RAW INQUIRY / HYPOTHESIS:                                                │
│ "Does solvent viscosity damp bacterial thermal velocity via Stokes' drag?"       │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 2. SCHOLARQA MECHANISTIC REFRAMING (THE "BETTER WAY"):                           │
│ "According to equipartition theory, what determines the instantaneous thermal    │
│  kinetic energy of a microscopic particle, and does fluid viscosity enter the    │
│  instantaneous velocity equation or only the velocity autocorrelation time?"     │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 3. DECOUPLED PHYSICAL DIMENSIONS:                                                │
│ • Instantaneous Velocity Magnitude: Governed by Equipartition (1/2 m v^2 = kT/2) │
│ • Velocity Autocorrelation Time: Governed by Stokes Drag (tau = m / 6 pi eta r)  │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 4. PREVENTED AI FAILURE MODE:                                                    │
│ 🛡️ Sycophantic Citation Bluffing (Misattributing Stokes drag to thermal speed)   │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Quick Start & Installation

### Option A: From Source
```bash
git clone https://github.com/your-username/scholarqa-reframer.git
cd scholarqa-reframer
pip install -e .
```

### Option B: Local Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 4. Usage

### Command-Line Interface (CLI)

Reframe an arbitrary question:
```bash
python -m scholarqa_reframer.cli "Does sound speed determine acoustic boundary reflection?"
```

Run on built-in benchmark samples (1=thermal velocity, 2=acoustic impedance, 3=membrane diffusion):
```bash
python -m scholarqa_reframer.cli --sample 1
```

Emit clean structured JSON for downstream pipeline ingestion:
```bash
python -m scholarqa_reframer.cli --sample 1 --json-output
```

### Interactive Streamlit Web UI

Launch the beautiful 3-pane interactive dashboard:
```bash
streamlit run app.py
```

Features:
- **Interactive Preset Selector:** Test benchmark questions from Physics, Biophysics, and Biochemistry.
- **3-Pane Split View:** Visual comparison of raw input vs. ScholarQA reframe vs. pedagogical critique.
- **Physical Dimensions Tab:** Visual cards detailing conflated user assumptions vs. rigorous laws.
- **One-Click Prompt Copy:** Easily paste the optimized prompt into ChatGPT, Claude, or NotebookLM.

---

## 5. Python API

```python
from scholarqa_reframer import MechanisticReframer

reframer = MechanisticReframer()

raw_query = "Does viscosity damp bacterial thermal velocity?"
result = reframer.reframe(raw_query)

print("ScholarQA Query:", result.scholarqa_mechanistic_query)
print("Core Principle:", result.core_governing_principle)
print("Avoided Failure:", result.avoided_failure_mode)

for probe in result.retrieval_probes:
    print(f"Probe: {probe.probe_name} -> {probe.search_keywords}")
```

---

## 6. How the Allen Reframing Algorithm Works

The reframing engine executes a 4-step formal transformation:

1. **Entity & Phenomenon Extraction:** Locates the physical systems (e.g. bacterium, fluid medium, acoustic boundary).
2. **Dimension Decoupling:** Identifies concepts that were conflated in the raw prompt (e.g. state functions vs. dissipative rates).
3. **Neutral Operator Injection:** Replaces binary check words (*"does X do Y?"*) with open inquiry operators (*"what fundamental principles determine..."*, *"how does X scale with Y under regime W..."*).
4. **Boundary Regime Specification:** Injects physical constraints (e.g. low Reynolds number $Re \ll 1$, thermal equilibrium, steady-state) required for unambiguous literature retrieval.

---

## 7. Running Tests

```bash
python -m unittest discover tests
```

---

## 8. License

MIT License. Designed and maintained by the Sanity Engine Core Architecture Team.
