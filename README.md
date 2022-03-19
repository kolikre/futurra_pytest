# futurra_pytest

**Requirements:**
- Python 3.8 +
- Pip 20 +

**How to set up project:**

1. Install virtual environment `python3 -m venv env`
2. Download chromedriver for your Chrome browser version from [here](https://chromedriver.chromium.org/downloads)
3. Unzip chromedriver to `env/bin/`
4. Raise up the virtual environment `source env/bin/activate` 
5. Install requirements `pip install -r requirments.txt`
6. Run all tests `pytest -v --junitxml="reports/test_result.xml"`

The test run report you can see at `reports/test_result.xml`
