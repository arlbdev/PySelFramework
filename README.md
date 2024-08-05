# Python Selenium Framework for Automation Testing

This project is a Selenium-based automation testing framework written in Python. It includes various features such as logging, data-driven testing, custom utilities, and integration with Jenkins for continuous integration.

## Features

- **Logging:** Implemented logging to track test execution.
- **Data-Driven Testing:** Parameterized tests with multiple data sets using a separate test data file.
- **Automated Screenshots:** Captures screenshots on test failure and generates HTML reports.
- **Custom Utilities:** Includes utilities for selecting dropdown options by text and verifying link presence.
- **Optimized Page Objects:** Enhanced page object mechanism for better maintainability and readability.
- **Jenkins Integration:** Configured to work with Jenkins, including creating a reports folder.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/arlbdev/PySelFramework
   cd your-repo-directory
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running Tests

To run the tests, use the following command:

```sh
pytest --browser_name=<browser_name>
```

You can also use the following to generate an html report:

```sh
pytest --browser_name=<browser_name> --html=reports.html
```

Replace `<browser_name>` with the desired browser (`chrome`, `firefox`, or `edge`). Make sure you are in the **tests** directory.

### Running Tests with Jenkins

The project is configured to integrate with Jenkins. Ensure Jenkins is set up and configured to execute the tests. The tests will generate a reports folder that contains the HTML report and screenshots of any failed tests.

## Project Structure

- **conftest.py:** Contains the setup configuration for pytest, including browser selection and screenshot capture on test failure.
- **test_e2e.py:** Contains end-to-end test cases.
- **test_HomePage.py:** Contains specific test cases for the Home Page functionality.
- **utilities:** Contains utility classes and methods, including base test class and custom utilities.
- **pageObjects:** Contains page object classes representing different pages of the application.
- **TestData:** Contains test data files.

## Test Cases

### test_HomePage.py

- **test_formSubmission:** Tests the form submission functionality on the home page. Parameters such as first name, email, and gender are provided from the test data file.

### test_e2e.py

- **test_e2e:** Tests the end-to-end functionality of adding an item to the cart, proceeding to checkout, and verifying the purchase.
