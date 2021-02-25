[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/PyTaintX.svg?style=for-the-badge)](../../)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/PyTaintX.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/PyTaintX.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/PyTaintX.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/PyTaintX.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/PyTaintX.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pytaintx.svg?style=for-the-badge)](https://pypistats.org/packages/pytaintx)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fpytaintx)](https://pepy.tech/project/pytaintx)
[![PyPI Version](https://img.shields.io/pypi/v/pytaintx.svg?style=for-the-badge)](https://pypi.org/project/pytaintx)

**Now Maintained**

<!-- omit in TOC -->
# PyTaintX

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Maintained branch of Python Taint for python 3.9

Static analysis of Python web applications based on theoretical
foundations (Control flow graphs, fixed point, dataflow analysis)

- [Features](#features)
- [How it Works](#how-it-works)
- [How to Use](#how-to-use)
- [Using](#using)
- [Using from Source](#using-from-source)
- [Virtual env setup guide](#virtual-env-setup-guide)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

## Features

-   Detect command injection, SSRF, SQL injection, XSS, directory
    traveral etc.
-   A lot of customisation possible

For a look at recent changes, please see the
[changelog](https://github.com/python-security/pytaintx/blob/master/CHANGELOG.md).

Example usage and output:

```
21 vulnerabilities found (plus 3 sanitised):
Vulnerability 1:
File: .\XSS.py
 > User input at line 6, source "request.args.get(":
         ~call_1 = ret_request.args.get('param', 'not set')
Reassigned in:
        File: .\XSS.py
         > Line 6: param = ~call_1
File: .\XSS.py
 > reaches line 9, sink "replace(":
        ~call_5 = ret_html.replace('{{ param }}', param)

[...]
```


## How it Works

Soon you will find a
[README.rst](https://github.com/python-security/pytaintx/tree/master/pytaintx) in
every directory in the `pytaintx/` folder, [start
here](https://github.com/python-security/pytaintx/tree/master/pytaintx).

## How to Use

1.  Choose a web framework

[The -a option determines which functions will have their arguments
tainted](https://github.com/python-security/pytaintx/tree/master/pytaintx/web_frameworks#web-frameworks),
by default it is Flask.

1.  (optional) Customize source and sink information

Use the `-t` option to specify sources and sinks, by default [this file
is
used](https://github.com/python-security/pytaintx/blob/master/pytaintx/vulnerability_definitions/all_trigger_words.pyt).

1.  (optional) Customize which library functions propagate taint

For functions from builtins or libraries, e.g. `url_for` or
`os.path.join`, use the `-m` option to specify whether or not they
return tainted values given tainted inputs, by [default this file is
used](https://github.com/python-security/pytaintx/blob/master/pytaintx/vulnerability_definitions/blackbox_mapping.json).

## Using

```
usage: python -m pytaintx [-h] [-a ADAPTOR] [-pr PROJECT_ROOT]
                     [-b BASELINE_JSON_FILE] [-j] [-t TRIGGER_WORD_FILE]
                     [-m BLACKBOX_MAPPING_FILE] [-i] [-o OUTPUT_FILE]
                     [--ignore-nosec] [-r] [-x EXCLUDED_PATHS]
                     [--dont-prepend-root] [--no-local-imports]
                     targets [targets ...]

required arguments:
  targets               source file(s) or directory(s) to be scanned

important optional arguments:
  -a ADAPTOR, --adaptor ADAPTOR
                        Choose a web framework adaptor: Flask(Default),
                        Django, Every or Pylons

  -t TRIGGER_WORD_FILE, --trigger-word-file TRIGGER_WORD_FILE
                        Input file with a list of sources and sinks

  -m BLACKBOX_MAPPING_FILE, --blackbox-mapping-file BLACKBOX_MAPPING_FILE
                            Input blackbox mapping file

optional arguments:
  -pr PROJECT_ROOT, --project-root PROJECT_ROOT
                        Add project root, only important when the entry file
                        is not at the root of the project.

  -b BASELINE_JSON_FILE, --baseline BASELINE_JSON_FILE
                        Path of a baseline report to compare against (only
                        JSON-formatted files are accepted)

  -j, --json            Prints JSON instead of report.

  -i, --interactive     Will ask you about each blackbox function call in
                        vulnerability chains.

  -o OUTPUT_FILE, --output OUTPUT_FILE
                        Write report to filename

  --ignore-nosec        Do not skip lines with # nosec comments

  -r, --recursive       Find and process files in subdirectories

  -x EXCLUDED_PATHS, --exclude EXCLUDED_PATHS
                        Separate files with commas

  --dont-prepend-root   In project root e.g. /app, imports are not prepended
                        with app.*

  --no-local-imports    If set, absolute imports must be relative to the
                        project root. If not set, modules in the same
                        directory can be imported just by their names.
```

## Using from Source

Using it like a user
`python3 -m pytaintx examples/vulnerable_code/XSS_call.py`

Running the tests `python3 -m tests`

Running an individual test file `python3 -m unittest tests.import_test`

Running an individual test
`python3 -m unittest tests.import_test.ImportTest.test_import`



## Virtual env setup guide

Create a directory to hold the virtual env and project

`mkdir ~/a_folder`

`cd ~/a_folder`

Clone the project into the directory

`git clone https://github.com/python-security/pytaintx.git`

Create the virtual environment

`python3 -m venv ~/a_folder/`

Check that you have the right versions

`python3 --version` sample output `Python 3.6.0`

`pip --version` sample output
`pip 9.0.1 from /Users/kevinhock/a_folder/lib/python3.6/site-packages (python 3.6)`

Change to project directory

`cd pytaintx`

In the future, just type `source ~/a_folder/bin/activate` to start
developing.


## Documentation
See the [Docs](/DOCS/) for more information.

## Install With PIP
```python
pip install pytaintx
```

Head to https://pypi.org/project/pytaintx/ for more info

## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.9.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.9
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.9 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.9)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## Download Project
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/PyTaintX
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files
### Licence
(See the [LICENSE](/LICENSE) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing
Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security
Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support
Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale
The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.
