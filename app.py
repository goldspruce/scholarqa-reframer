"""
Streamlit Web Application: ScholarQA Mechanistic Query Reframer
A pedagogical scientific pre-processor that demonstrates how to frame unbiased, multi-dimensional inquiries.
"""

import streamlit as st
import json
from scholarqa_reframer.engine import MechanisticReframer, GOLDEN_BENCHMARK_ARCHETYPES

# Page Configuration
st.set_page_config(
    page_title="ScholarQA Mechanistic Query Reframer",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.1rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #64748b;
        margin-bottom: 1.6rem;
    }
    .card-raw {
        background-color: #fffbeb;
        border: 1px solid #fde68a;
        border-left: 5px solid #f59e0b;
        padding: 16px 20px;
        border-radius: 6px;
        margin-bottom: 16px;
    }
    .card-reframe {
        background-color: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-left: 5px solid #10b981;
        padding: 20px 24px;
        border-radius: 6px;
        margin-bottom: 16px;
    }
    .card-pedagogy {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 5px solid #0ea5e9;
        padding: 18px 22px;
        border-radius: 6px;
        margin-bottom: 16px;
    }
    .label-tag {
        font-size: 0.76rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .reframe-text {
        font-size: 1.15rem;
        font-weight: 600;
        color: #065f46;
        line-height: 1.5;
    }
    .dim-box {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        padding: 12px 16px;
        border-radius: 6px;
        margin-top: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar: Preset Samples & Options
st.sidebar.title("🔬 Query Presets")
st.sidebar.markdown("Select a sample benchmark inquiry or type your own:")

PRESET_OPTIONS = {
    "Custom Inquiry": "",
    "Q2: Bacterial Thermal Velocity (Berg)": "Does solvent viscosity damp bacterial instantaneous thermal velocity according to Stokes' drag?",
    "Q3: Acoustic Impedance & Reflection (Feynman)": "Does characteristic sound speed determine the acoustic boundary reflection coefficient?",
    "Q5: Lipid Bilayer Permeability (Alberts)": "Does passive diffusion of small molecules across a lipid bilayer require metabolic ATP transport?",
    "Q6: Conductor Skin Depth (Feynman Vol. 2)": "Does electromagnetic wave skin depth scale linearly with wave frequency?",
    "Q9: Michaelis-Menten Kinetics (Lehninger)": "Does the substrate-enzyme complex concentration remain constant throughout the entire reaction?"
}

selected_preset = st.sidebar.selectbox("Choose a Benchmark Sample:", list(PRESET_OPTIONS.keys()))
default_text = PRESET_OPTIONS[selected_preset] if selected_preset != "Custom Inquiry" else ""

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 About ScholarQA Reframing")
st.sidebar.info(
    "Frontier LLMs suffer from **sycophancy** when fed closed questions. "
    "The **Allen Institute ScholarQA** methodology reframes inquiries into open, "
    "multi-dimensional mechanistic investigations. This removes confirmation bias and "
    "retrieves high-signal physical derivations."
)

# Main Title Area
st.markdown('<div class="main-header">Mechanistic Query Reframer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">Transform leading, closed hypotheses into open, multi-dimensional ScholarQA research inquiries.</div>',
    unsafe_allow_html=True
)

# User Input Box
user_query = st.text_area(
    "Enter a scientific question, leading hypothesis, or research problem:",
    value=default_text or "Does solvent viscosity damp a bacterium's instantaneous thermal velocity according to Stokes' drag?",
    height=90,
    placeholder="e.g. Does solvent viscosity damp bacterial thermal velocity?"
)

col_run, col_clear = st.columns([1, 5])
with col_run:
    run_btn = st.button("⚡ Reframe Inquiry", type="primary")

if user_query and (run_btn or default_text):
    reframer = MechanisticReframer()
    with st.spinner("Analyzing physical dimensions and reframing inquiry..."):
        result = reframer.reframe(user_query)

    # 3-PANE OUTPUT LAYOUT
    st.markdown("---")

    # Pane 1: Raw Inquiry Summary
    st.markdown(f"""
    <div class="card-raw">
        <div class="label-tag" style="color: #b45309;">1. Original User Input (Closed / Leading Formulation):</div>
        <div style="font-size: 1.05rem; color: #78350f;">"{result.original_query}"</div>
    </div>
    """, unsafe_allow_html=True)

    # Pane 2: The ScholarQA Reframed Formulation
    st.markdown(f"""
    <div class="card-reframe">
        <div class="label-tag" style="color: #047857;">2. ScholarQA Mechanistic Reframing (The "Better Way"):</div>
        <div class="reframe-text">"{result.scholarqa_mechanistic_query}"</div>
        <div style="margin-top: 10px; font-size: 0.88rem; color: #047857;">
            <strong>Core Invariant:</strong> {result.core_governing_principle}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Copy / Action helpers
    st.code(result.scholarqa_mechanistic_query, language="text")

    # Pane 3: Pedagogical Critique & Decoupled Dimensions
    st.markdown(f"""
    <div class="card-pedagogy">
        <div class="label-tag" style="color: #0284c7;">3. Why This Reframing is Superior (Pedagogy & Retrieval Precision):</div>
        <div style="font-size: 0.95rem; color: #1e293b; margin-bottom: 12px;">{result.pedagogical_critique}</div>
        <div style="font-size: 0.88rem; color: #0f172a; font-weight: 600;">
            🛡️ Avoided Failure Mode: <span style="color: #166534;">{result.avoided_failure_mode}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs for Detailed Breakdown
    tab_dim, tab_probes, tab_regimes, tab_json = st.tabs([
        "🧩 Decoupled Physical Dimensions",
        "🔍 High-Signal Retrieval Probes",
        "📐 Boundary Regimes & Constraints",
        "📄 Structured JSON Schema"
    ])

    with tab_dim:
        st.markdown("#### Physical Dimensions Conflated by User Prompt vs. Rigorous Law")
        for dim in result.decoupled_dimensions:
            with st.container():
                st.markdown(f"""
                <div class="dim-box">
                    <h5 style="margin: 0 0 6px 0; color: #0f172a;">{dim.dimension_name}</h5>
                    <p style="margin: 0 0 4px 0; font-size: 0.88rem; color: #991b1b;">
                        <strong>Conflated User Assumption:</strong> {dim.conflated_role}
                    </p>
                    <p style="margin: 0 0 4px 0; font-size: 0.88rem; color: #166534;">
                        <strong>Rigorous Physical Role:</strong> {dim.rigorous_role}
                    </p>
                    <p style="margin: 0; font-size: 0.88rem; font-family: monospace; color: #0284c7;">
                        <strong>Governing Invariant:</strong> {dim.governing_equation_or_rule}
                    </p>
                </div>
                """, unsafe_allow_html=True)

    with tab_probes:
        st.markdown("#### High-IDF Search Probes (Direct Target Textbook Anchors)")
        for probe in result.retrieval_probes:
            st.markdown(f"- **{probe.probe_name}**")
            st.code(probe.search_keywords, language="text")
            st.caption(f"🎯 Target Literature: {probe.target_corpus_anchor}")

    with tab_regimes:
        st.markdown("#### Required Boundary Conditions & Physical Regimes")
        for regime in result.boundary_regimes:
            st.markdown(f"- `{regime}`")

    with tab_json:
        st.json(result.model_dump())
