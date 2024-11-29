# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12
installed. You will also need the following libraries (minimum versions in brackets)

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation 

## Installation instructions
Clone the repository
```bash 
git clone https://github.com/ThWacker/FAIR_course.git
```
Navigate to the folder with the code 

```bash
cd astronaut-data-analysis-not-so-fair-main/
```

Create an environment and install all required dependencies 

```bash
#create environment
python3 -m venv my_env
#activate environment
source my_env/bin/activate
#install all dependencies
pip install -r requirements.txt
```
To ensure everything is working correctly, run the tests using pytest.

```python
python3 -m pytest
```

## Basic Usage

In the simplest case, you can just run:

```bash
python3 eva_data_analysis.py
```

You can also explicitely define input and output files as positional arguments:

```bash
python3 eva_data_analysis input.json output.csv 
```

As an input, the .json in the data folder should be used, specifically that would be:

```bash
python3 eva_data_analysis ./data/eva-data.json output.csv 
```

## License 
MIT License

Copyright (c) [2024] [Theresa Wacker]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.