# Python Unittest Model
The project utilizes the python unittest model to ensure the functionalities of its models. The following sample script runs a test model: ```python -m unittest tests/```
All tests should also pass in non-interactive mode:
$ echo "python3 -m unittest discover tests" | bash
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py