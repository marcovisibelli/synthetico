# Synthetico

[![Build Status](https://travis-ci.org/benkeen/generatedata.png?branch=master)](https://travis-ci.org/benkeen/generatedata)

![Data](media/Data.png?raw=true "Data example")


Synthetico is a ready to use general-purpose synthetic data generators to enable data science experiments. The program is an engine to generate any sort of random data (name,surnames, telephon namebers, emails) from many nations (6 currently). Let you to create business data for multiple business scenarios (Web portals, CRM data, E-commerce data, ERP data etc) that can be reaplced in a second time with real ones. I created Syntetico because all the commercial synthetic generators are way to much expensive or too much complicated to use. Some of the features:

* Names and surnames from more than 6 countries (UK,France,Germany,Italy,Spain and Greece)
* Phone numbers with template support
* Categories based on probability distribution

# Prerequisites

The application need a set of modules:

```pip3 install -r requirements.txt```

# Installing

Clone the repository into a folder.

# Running the tests
To run the application just execute the main.py:

```python example_ERP_data.py ```

In this example two csv files will be created in the data folder.

# Getting Started

TBD

# License

This project is licensed under the MIT License

# Changelog


1.1.1 - 15/10/2018
- Phone number support

1.1.0 - 02/10/2018
- New relaese

1.0.0 - 02/03/2017
- Initial release
