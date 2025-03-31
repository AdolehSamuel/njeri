#!/usr/bin/env python3

"""
User Interface module for Njeri application
Handles all user interactions and display formatting
"""

import os
import time
import platform
from dataclasses import dataclass
from typing import Dict, Any, Optional
from .config import Colors, APP_NAME, APP_TAGLINE, APP_POWERED_BY
from .config import FILTER_SETS


@dataclass
class SearchParameters:
    """Data class to store search parameters"""

    keyword: str
    location: str
    filters: Dict[str, str]


class UserInterface:
    """Class handling all user interface elements and interactions"""

    def clear_screen(self):
        """Clear the terminal screen based on operating system"""
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def display_welcome_screen(self):
        """Display a flashy welcome screen with pink colors"""
        self.clear_screen()

        welcome_text = f"""
        {Colors.PINK}{Colors.BOLD}
        *********************************************
        *                                           *
        *               Welcome to                  *
        *                                           *
        *       NN    N   JJJJJ  EEEEE  RRRR  IIIII *
        *       N N   N     J    E      R   R   I   *
        *       N  N  N     J    EEE    RRRR    I   *
        *       N   N N  J  J    E      R  R    I   *
        *       N    NN   JJ     EEEEE  R   R  IIIII*
        *                                           *
        *        Your Journey to Career Success     *
        *                                           *
        *********************************************
        {Colors.END}

        {APP_TAGLINE}
        We're here to make job searching easier and more accessible for women.
        
        {APP_POWERED_BY}
        """

        print(welcome_text)
        time.sleep(2)  # Give users time to read the welcome message

    def get_job_keyword(self) -> str:
        """Ask the user for job search keywords"""
        print(f"\n{Colors.PINK}JOB SEARCH{Colors.END}")
        print("What kind of job are you looking for?")
        print("Examples: Software Engineer, Marketing Manager, Data Analyst, etc.")

        while True:
            keyword = input(
                f"\n{Colors.PINK}Enter job title or keywords:{Colors.END} "
            ).strip()
            if keyword:
                return keyword
            print("Please enter at least one keyword to continue.")

    def get_job_location(self) -> str:
        """Ask the user for the desired job location"""
        print(f"\n{Colors.PINK}JOB LOCATION{Colors.END}")
        print("Where would you like to work?")
        print("You can enter a city, state, or 'Remote' for remote opportunities.")

        location = input(
            f"\n{Colors.PINK}Enter location (or press Enter for any location):{Colors.END} "
        ).strip()
        return location

    def _get_filter_selection(self, filter_type: str, title: str) -> Optional[str]:
        """Generic method to get filter selection from user"""
        filter_options = FILTER_SETS[filter_type]

        print(f"\n{Colors.PINK}{title}:{Colors.END}")
        for option in filter_options:
            print(f"{option.id}. {option.name}")

        valid_choices = [str(option.id) for option in filter_options]
        choice = input(
            f"\n{Colors.PINK}Select option (0-{len(filter_options)-1}):{Colors.END} "
        ).strip()

        if choice in valid_choices:
            choice_id = int(choice)
            # Return None if "No preference", otherwise return the parameter value
            return next(
                (
                    option.param_value
                    for option in filter_options
                    if option.id == choice_id
                ),
                None,
            )

        return None

    def get_additional_filters(self) -> Dict[str, str]:
        """Ask the user for additional job filtering options"""
        filters = {}

        print(f"\n{Colors.PINK}ADDITIONAL FILTERS{Colors.END}")
        print("Let's narrow down your search with some additional filters.")

        # Job Type Filter
        job_type = self._get_filter_selection("job_type", "Job Type")
        if job_type:
            filters["job_type"] = job_type

        # Experience Level Filter
        experience = self._get_filter_selection("experience", "Experience Level")
        if experience:
            filters["experience"] = experience

        # Compensation Filter
        salary = self._get_filter_selection("salary", "Minimum Salary")
        if salary:
            filters["salary"] = salary

        # Remote Work Filter
        remote = self._get_filter_selection("remote", "Remote Work")
        if remote:
            filters["remote"] = remote

        return filters

    def collect_search_parameters(self) -> SearchParameters:
        """Collect all search parameters from the user"""
        keyword = self.get_job_keyword()
        location = self.get_job_location()
        filters = self.get_additional_filters()

        return SearchParameters(keyword=keyword, location=location, filters=filters)

    def display_search_results(self, params: SearchParameters, url: str):
        """Display the search results and confirmation to the user"""
        self.clear_screen()
        print(
            f"\n{Colors.PINK}{Colors.BOLD}Perfect! We've found some great opportunities for you.{Colors.END}"
        )
        print("\nOpening Fairygodboss job search in your browser...")
        print(
            f"Search criteria: {params.keyword} in {params.location or 'Any Location'}"
        )

        # Display applied filters
        if params.filters:
            print("\nFilters applied:")
            for key, value in params.filters.items():
                filter_name = key.replace("_", " ").title()
                filter_options = FILTER_SETS.get(key, [])

                # Find the display name for this filter value
                filter_display = next(
                    (
                        option.name
                        for option in filter_options
                        if option.param_value == value
                    ),
                    value,
                )
                print(f"- {filter_name}: {filter_display}")

        print(f"\nURL: {url}")
        print(
            "\nIf your browser doesn't open automatically, you can copy and paste the URL above."
        )
        time.sleep(2)

    def ask_continue_search(self) -> bool:
        """Ask if the user wants to perform another search"""
        while True:
            again = input(
                f"\n{Colors.PINK}Would you like to perform another search? (y/n):{Colors.END} "
            ).lower()
            if again == "y":
                self.clear_screen()
                return True
            elif again == "n":
                return False
            else:
                print("Please enter 'y' or 'n'.")

    def display_exit_message(self):
        """Display exit message to the user"""
        print(
            f"\n{Colors.PINK}{Colors.BOLD}Thank you for using {APP_NAME}! "
            f"Wishing you success on your career journey!{Colors.END}"
        )

    def display_interrupted_message(self):
        """Display message when program is interrupted"""
        print(
            f"\n\n{Colors.PINK}Program interrupted. Thank you for using {APP_NAME}!{Colors.END}"
        )
