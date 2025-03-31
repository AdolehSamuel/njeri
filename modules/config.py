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

FilterOption = namedtuple("FilterOption", ["id", "name", "param_value"])

# Job Types
JOB_TYPES = [
    FilterOption(0, "No preference", None),
    FilterOption(1, "Full-time", "fulltime"),
    FilterOption(2, "Part-time", "parttime"),
    FilterOption(3, "Contract", "contract"),
    FilterOption(4, "Internship", "internship"),
]

# Experience Levels
EXPERIENCE_LEVELS = [
    FilterOption(0, "No preference", None),
    FilterOption(1, "Entry Level", "entry"),
    FilterOption(2, "Mid Level", "mid"),
    FilterOption(3, "Senior Level", "senior"),
    FilterOption(4, "Executive", "executive"),
]

# Salary Ranges
SALARY_RANGES = [
    FilterOption(0, "No preference", None),
    FilterOption(1, "$30,000+", "30000"),
    FilterOption(2, "$50,000+", "50000"),
    FilterOption(3, "$75,000+", "75000"),
    FilterOption(4, "$100,000+", "100000"),
    FilterOption(5, "$150,000+", "150000"),
]

# Remote Work Options
REMOTE_OPTIONS = [
    FilterOption(0, "No preference", None),
    FilterOption(1, "Remote only", "remote"),
    FilterOption(2, "Hybrid", "hybrid"),
    FilterOption(3, "On-site only", "onsite"),
]

# Define a dictionary mapping filter types to their option sets
FILTER_SETS = {
    "job_type": JOB_TYPES,
    "experience": EXPERIENCE_LEVELS,
    "salary": SALARY_RANGES,
    "remote": REMOTE_OPTIONS,
}


# Terminal Colors
class Colors:
    PINK = "\033[95m"
    BOLD = "\033[1m"
    END = "\033[0m"
