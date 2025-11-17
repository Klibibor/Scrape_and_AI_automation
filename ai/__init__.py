"""
AI Cover Letter Generation Module
=================================
Provides AI-powered cover letter generation for Upwork jobs
"""

# CoverLetterGenerator removed - using SmartCoverLetterGenerator in scripts/ instead
from .local_ai import LocalAIProvider
from .openai import OpenAIProvider
from .model_training import CoverLetterTrainer

__all__ = ['LocalAIProvider', 'OpenAIProvider', 'CoverLetterTrainer']