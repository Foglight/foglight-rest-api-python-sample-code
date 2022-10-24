# Foglight REST API sample code

This is an python sample to call Foglight restful API.
## Files

| File Name | Description |
| ------ | ------ |
| `__init__.cfg` | configuration file, configure username, password and so on. |
| `__init__.py` | http client utility for call Foglight restful APIs. |
| `sample-login.py` | python sample for call login related restful APIs. |
| `sample.py` | python sample for call login-excluded restful APIs. |
| `requirements.txt` | requirements file for package dependencies not included in the standard library. |

## Usage and setup

Before run the sample, you'll need to create a virtual environment and install the dependencies in the `requirements.txt` file.

1. Create Virtual Environment: `python -m venv venv`
2. Activate `venv`: `.\venv\scripts\Activate.ps1`
3. Install dependencies: `python -m pip install -r .\requirements.txt`

For more information about virtual environments, please review the [official documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Next, you'll need to configure the parameters in `__init__.cfg`, then you can run either `sample-login.py` or `sample.py`.

Some of the call methods are commented inside `sample.py`, you need to configure the related parameters in `__init__.cfg`, and then you can uncomment the methods to run the samples.
