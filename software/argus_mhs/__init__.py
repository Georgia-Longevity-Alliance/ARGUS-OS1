"""argus_mhs — MHS-style driver layer for ARGUS (Model Hardware Standard alignment).

Tool Bridge alignment with Anthropic's Model Hardware Standard (MHS):
standardized driver abstraction with two primitives (read / write),
discoverability, natural-language safety tags, and a Safety Layer
(Body Law). Transport: MCP / CLI / code files.

Reference: docs/MHS_MODEL_HARDWARE_STANDARD_ANALYSIS.md (section 4)
"""
from .driver import MHSDriver, Tag

__all__ = ["MHSDriver", "Tag"]
__version__ = "0.1.0"
