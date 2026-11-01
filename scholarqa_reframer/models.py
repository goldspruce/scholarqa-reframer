"""
Pydantic data models for the ScholarQA Mechanistic Query Reframer.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class DecoupledDimension(BaseModel):
    """Represents a specific physical/biological variable disentangled from the prompt."""
    dimension_name: str = Field(description="Name of the physical or biological variable/concept")
    conflated_role: str = Field(description="How the user's raw prompt conflated or misattributed this concept")
    rigorous_role: str = Field(description="The true physical behavior or functional relationship")
    governing_equation_or_rule: str = Field(description="The mathematical formula or biochemical invariant")


class RetrievalProbe(BaseModel):
    """High-signal keyword set designed to target physical derivations on disk."""
    probe_name: str = Field(description="Descriptive name of the search probe")
    search_keywords: str = Field(description="High-IDF search tokens optimized for BM25/Vector retrieval")
    target_corpus_anchor: str = Field(description="Specific literature reference or chapter where derivation lives")


class ReframedInquiry(BaseModel):
    """Complete structured transformation of a scientific query."""
    original_query: str = Field(description="The raw, closed, or leading question input by the user")
    scholarqa_mechanistic_query: str = Field(description="The open, multi-dimensional ScholarQA inquiry")
    core_governing_principle: str = Field(description="The fundamental physical law or biochemical mechanism")
    decoupled_dimensions: List[DecoupledDimension] = Field(default_factory=list, description="Independent physical dimensions disentangled")
    boundary_regimes: List[str] = Field(default_factory=list, description="Explicit boundary conditions and assumptions")
    retrieval_probes: List[RetrievalProbe] = Field(default_factory=list, description="High-IDF search queries for downstream literature search")
    pedagogical_critique: str = Field(description="Pedagogical explanation of why this framing is superior")
    avoided_failure_mode: str = Field(description="The specific AI failure mode prevented (e.g. sycophancy, citation bluffing)")
