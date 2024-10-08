## Test automation framework for testing UI web site - https://demoqa.com/

## Table of contents
1. [Test framework configuration and setup](#test-framework-configuration-and-setup)
2. [Preparation before running tests](#preparation-before-running-tests)
3. [Tests](#tests)

### Test framework configuration and setup

In this project used 'pip-tools'. All used Python packages for the current project are generates in requirements.txt
Below is the list of main packages with references

### **For test itself**
### pytest

related info: https://docs.pytest.org/en/latest/

    pip install pytest
## **For ui/web testing**

### selenium

related info: https://selenium-python.readthedocs.io/

    pip install selenium

### webdriver-manager

related info:https://github.com/bonigarcia/webdrivermanager

    pip install webdriver-manager


## **Data generators**

### Faker

related info: http://faker.rtfd.org/

    pip install Faker


## Preparation before running tests
Create virtual environment.
To create a virtual environment, execute the following commands in the command line:

    pip install virtualenv
    pip install virtualenvwrapper-win

To activate the virtual environment:

```bash
venv\Scripts\activate
```

All used packages are stored in requirements.txt

    pip install -r requirements.txt


## Tests

All tests are located in  ***tests*** folder

To run all the tests from the root directory, you can use the following command:
```shell
 pytest
```
   

To run a specific test, use the command, where * this is the name of the test.:
```bash
pytest tests/elements_test/*.py
```