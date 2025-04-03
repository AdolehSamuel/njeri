# Application Information
APP_NAME = "Njeri"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Your Journey to Career Success"
APP_TAGLINE = (
    'Njeri means "traveler" in Kenyan, representing your journey to career success.'
)
APP_POWERED_BY = "Powered by Fairygodboss resources"

# URL Configuration
FAIRYGODBOSS_BASE_URL = "https://fairygodboss.com/jobs/find"

# Filter Options - Using named tuples for immutable data structures
from collections import namedtuple
import json
import os

FilterOption = namedtuple("FilterOption", ["id", "name", "param_value"])

# Path to database.json (relative to the project root)
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database.json")

# Load filter options from database.json
def load_filter_options():
    try:
        with open(DB_PATH, 'r') as file:
            data = json.load(file)
            
        # Convert JSON data to FilterOption named tuples
        filter_sets = {}
        for filter_type, options in data.items():
            filter_sets[filter_type] = [
                FilterOption(
                    id=option["id"],
                    name=option["name"],
                    param_value=option["param_value"]
                )
                for option in options
            ]
        return filter_sets
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading database.json: {e}")
        # Fall back to default filter options
        return {
            "job_type": [
                FilterOption(0, "No preference", None),
                FilterOption(1, "Full-time", "fulltime"),
                FilterOption(2, "Part-time", "parttime"),
                FilterOption(3, "Contract", "contract"),
                FilterOption(4, "Internship", "internship"),
            ],
            "experience": [
                FilterOption(0, "No preference", None),
                FilterOption(1, "Entry Level", "entry"),
                FilterOption(2, "Mid Level", "mid"),
                FilterOption(3, "Senior Level", "senior"),
                FilterOption(4, "Executive", "executive"),
            ],
            "salary": [
                FilterOption(0, "No preference", None),
                FilterOption(1, "$30,000+", "30000"),
                FilterOption(2, "$50,000+", "50000"),
                FilterOption(3, "$75,000+", "75000"),
                FilterOption(4, "$100,000+", "100000"),
                FilterOption(5, "$150,000+", "150000"),
            ],
            "remote": [
                FilterOption(0, "No preference", None),
                FilterOption(1, "Remote only", "remote"),
                FilterOption(2, "Hybrid", "hybrid"),
                FilterOption(3, "On-site only", "onsite"),
            ]
        }

# Load filter options
FILTER_SETS = load_filter_options()

# Terminal Colors
class Colors:
    PINK = "\033[95m"
    BOLD = "\033[1m"
    END = "\033[0m"
