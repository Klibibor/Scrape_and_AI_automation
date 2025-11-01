"""
Cover Letter Generator
======================
Main module for AI-powered cover letter generation
"""

import logging
from typing import Dict, Any, Optional, List
from pathlib import Path

from .local_ai import LocalAIProvider
from .openai import OpenAIProvider

logger = logging.getLogger(__name__)

class CoverLetterGenerator:
    """Main cover letter generator that can use different AI providers"""

    def __init__(self, preferred_provider: str = "openai"):
        """
        Initialize the cover letter generator

        Args:
            preferred_provider: "openai" or "local_ai"
        """
        self.preferred_provider = preferred_provider
        self.providers = {
            "local_ai": LocalAIProvider(),
            "openai": OpenAIProvider()
        }

    def generate_cover_letter(self, job_data: Dict[str, Any], provider: Optional[str] = None) -> str:
        """
        Generate a cover letter for a job

        Args:
            job_data: Dictionary containing job information
            provider: Specific provider to use ("openai" or "local_ai")

        Returns:
            Generated cover letter text
        """
        provider_name = provider or self.preferred_provider
        provider_instance = self.providers.get(provider_name)

        if not provider_instance:
            return f"Provider '{provider_name}' not found"

        if not provider_instance.is_available():
            # Try fallback provider
            fallback_provider = "local_ai" if provider_name == "openai" else "openai"
            logger.warning(f"{provider_name} not available, trying {fallback_provider}")
            provider_instance = self.providers.get(fallback_provider)

            if not provider_instance or not provider_instance.is_available():
                return f"No AI providers available. Please check configuration."

        try:
            cover_letter = provider_instance.generate_cover_letter(job_data)
            return cover_letter
        except Exception as e:
            logger.error(f"Error generating cover letter: {e}")
            return f"Error generating cover letter: {str(e)}"

    def get_available_providers(self) -> List[str]:
        """Get list of available providers"""
        return [name for name, provider in self.providers.items() if provider.is_available()]

    def set_preferred_provider(self, provider: str):
        """Set the preferred AI provider"""
        if provider in self.providers:
            self.preferred_provider = provider
        else:
            raise ValueError(f"Unknown provider: {provider}")