# Playwright Python UI Testing Framework with Jenkins Parallel Execution

This repository contains a mid-level UI automation testing project built with **Playwright (Python)** and **PyTest**, implementing the **Page Object Model (POM)** design pattern. It demonstrates parallel continuous integration testing across multiple Jenkins nodes.

## Project Purpose
The purpose of this project is to automate realistic end-to-end UI workflows on the demo website `saucedemo.com`. By structuring the tests efficiently and providing a `Jenkinsfile`, it highlights standard practices for industry-level CI/CD pipeline integration and scalable UI testing.

## Framework Structure
```plaintext
playwright-jenkins-parallel-framework/
│
├── tests/                 # Contains the PyTest test scripts
│   ├── conftest.py        # PyTest fixtures and configurations
│   ├── test_login.py      # Automation for Login flows
│   ├── test_cart.py       # Automation for add-to-cart flows
│   ├── test_checkout.py   # Automation for the checkout flow
│
├── pages/                 # Contains the Page Object Model classes
│   ├── login_page.py      # Elements and actions for the Login page
│   ├── cart_page.py       # Elements and actions for the Cart/Inventory pages
│   ├── checkout_page.py   # Elements and actions for the Checkout pages
│
├── utils/                 # Shared utilities  
│   ├── base_page.py       # BasePage class with common Playwright operations
│
├── requirements.txt       # Project dependencies
├── pytest.ini             # PyTest configurations (base URL, markers, standard args)
└── Jenkinsfile            # Declarative pipeline for Jenkins parallel execution
```

## How to Run Tests Locally

### Prerequisites
- Python 3.8+ installed
- `pip` installed

### Setup
1. Clone this repository and navigate to the project directory:
   ```bash
   cd playwright-jenkins-parallel-framework
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install the Playwright browser binaries (Chromium):
   ```bash
   playwright install chromium
   ```

### Running the Tests
To run all tests:
```bash
pytest
```

To run a specific test file:
```bash
pytest tests/test_login.py
```

*Note: Screenshots and traces will be automatically generated upon test failure.*

## Jenkins Pipeline Execution
The included `Jenkinsfile` demonstrates how these tests can run in parallel across two separate Jenkins agents (nodes). This drastically reduces the total execution time of the CI/CD pipeline.

### Pipeline Architecture
The declarative pipeline consists of two parallel stages:
1. **Node 1 - Login Tests**: 
   - Uses the Jenkins label `playwright-node-1`.
   - Checks out the code, installs dependencies/browsers, and executes `tests/test_login.py`.
2. **Node 2 - Cart & Checkout Tests**: 
   - Uses the Jenkins label `playwright-node-2`.
   - Checks out the code, installs dependencies/browsers, and executes `tests/test_cart.py` and `tests/test_checkout.py`.

### Execution Flow per Node
1. **Checkout**: Pulls the latest code from the Git repository.
2. **Install Dependencies**: Runs `pip install -r requirements.txt`.
3. **Install Browsers**: Runs `playwright install chromium`. 
4. **Run PyTest**: Executes PyTest and outputs JUnit XML reports.

After execution, Jenkins will collect the JUnit XML results and securely archive any generated failure screenshots or traces.
