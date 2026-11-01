"""
ScholarQA Mechanistic Query Reframer
Transforms leading closed scientific hypotheses into open, multi-dimensional ScholarQA inquiries.
"""

from .models import ReframedInquiry, DecoupledDimension, RetrievalProbe
from .engine import MechanisticReframer

__version__ = "0.1.0"
__all__ = ["ReframedInquiry", "DecoupledDimension", "RetrievalProbe", "MechanisticReframer"]
