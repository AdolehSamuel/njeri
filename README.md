# Njeri Job Search Application

A simple menu-driven Python application that makes job searching for women seamless by connecting users to real-world career opportunities through Fairygodboss.

## Project Background

Njeri is a feminine Kenyan word meaning "traveler," representing the journey to career success. Our mission is to make job searching easier and more accessible for women by providing career guidance and resources.

## Features

- Simple, flashy welcome screen with pink color theme
- Search for jobs based on keywords
- Filter by location and other parameters
- Connect directly to Fairygodboss job listings with your specified filters
- User-friendly terminal interface

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/your-org/njeri-job-search.git
   cd njeri-job-search
   ```

2. Install the package:
   ```
   pip install -e .
   ```

## Usage

You can run the application directly:

```
python main.py
```

Or use the console script if you've installed the package:

```
njeri
```

## Project Structure

```
njeri-job-search/
├── main.py                  # Main application entry point
├── setup.py                 # Setup file for installation
├── README.md                # Project documentation
└── modules/                 # Application modules
    ├── __init__.py          # Package initialization
    ├── config.py            # Configuration and constants
    ├── ui.py                # User interface components
    └── job_search.py        # Job search functionality
```

## Requirements

- Python 3.6 or higher
- Internet connection to access Fairygodboss

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request
