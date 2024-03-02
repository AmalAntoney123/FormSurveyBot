# Form Fill Bot using Selenium

## Project Overview

This project is a Python script that utilizes the Selenium library to automate the filling of a Google Form. The script simulates user interaction by randomly selecting options from predefined sets of buttons, providing a way to generate multiple form responses programmatically.

## Dependencies

- Python 3.x
- Selenium library
- Microsoft Edge WebDriver (or any other WebDriver of your choice)

## Setup

1. Install Python: [Download Python](https://www.python.org/downloads/)
2. Install Selenium: `pip install selenium`
3. Download the Microsoft Edge WebDriver: [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Usage

1. Replace the `google_form_url` variable with the URL of your Google Form.
2. Define your list of XPaths for button clicks in `button_xpaths1` and `button_xpaths2`.
3. Adjust the `limit` variable to set the number of form responses needed.
4. Run the script using the command: `python form_fill_bot.py`

## Variables to Customize

1. `google_form_url`: Replace with the actual URL of your Google Form.
2. `button_xpaths1`: List of XPaths for options.
3. `button_xpaths2`: List of XPaths for multiple choice options.
3. `submitXpath`: XPaths for submit button.
4. `limit`: Number of form responses needed.

## Important Notes

- Ensure that you have the correct WebDriver installed and its path added to your system environment variables.
- Make sure to review and adjust XPaths based on the structure of your Google Form.

## Disclaimer

Use this script responsibly and in accordance with the terms of service of the platform you are interacting with. Automated interactions with websites may violate their terms of service.

Feel free to customize the script to suit your specific form structure and requirements. Happy form filling!
