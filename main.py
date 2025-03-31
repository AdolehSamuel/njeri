#!/usr/bin/env python3
"""
Njeri - A job search application for women
Main application file that orchestrates the program flow
"""

import sys
from modules.ui import UserInterface
from modules.job_search import JobSearchService


def main():
    """Main function to run the Njeri application."""
    try:
        # Initialize UI and services
        ui = UserInterface()

        job_service = JobSearchService()

        # Show welcome screen
        ui.display_welcome_screen()

        # Main application loop
        while True:
            # Get search parameters from user
            search_params = ui.collect_search_parameters()

            # Process search and get URL
            search_url = job_service.create_search_url(search_params)

            # Display and open results
            ui.display_search_results(search_params, search_url)
            job_service.open_in_browser(search_url)

            # Check if user wants to continue
            if not ui.ask_continue_search():
                ui.display_exit_message()
                break

    except KeyboardInterrupt:
        ui = UserInterface()  # Create UI instance if not already created
        ui.display_interrupted_message()
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again later.")
        sys.exit(1)


if __name__ == "__main__":
    main()
