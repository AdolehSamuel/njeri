import webbrowser
import urllib.parse
from typing import Dict, Any
from .ui import SearchParameters
from .config import FAIRYGODBOSS_BASE_URL


class JobSearchService:
    """Service class for job search operations"""

    def create_search_url(self, params: SearchParameters) -> str:
        """Create a search URL with the specified parameters"""
        # Build the query parameters
        query_params = {}

        if params.keyword:
            query_params["q"] = params.keyword

        if params.location:
            query_params["location"] = params.location

        # Add additional filters to the parameters
        query_params.update(params.filters)

        # Construct the full URL
        query_string = urllib.parse.urlencode(query_params)
        full_url = f"{FAIRYGODBOSS_BASE_URL}?{query_string}"

        return full_url

    def open_in_browser(self, url: str) -> None:
        """Open the provided URL in the default browser"""
        webbrowser.open(url)
