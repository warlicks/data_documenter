#!/usr/bin/env python

"""Tests for `data_documenter` package."""

import pytest
import pandas as pd


from datadoc import DataDocumenter


@pytest.fixture
def input_data_frame():
    data = {'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'col2': ['M', 'F', 'M', 'F', 'M', 'M', 'M', None, 'F', 'F'],
            'col3': [2.2, 3.45, 1.2, 1.1, 5.0, 4.44, 56.6, 2.4, 5, 33.333]}
    return pd.DataFrame(data)


@pytest.fixture
def var_name_expected():
    """Creates expected output for test_variable_names"""
    return pd.DataFrame({'variable_name': ['col1', 'col2', 'col3'],
                         'variable': ['Age in years', 'Gender', 'Measure']})


@pytest.fixture
def var_definition_expected():
    """Creates expected output for test_variable_names"""
    string1 = 'The age of the participant when they joined'
    string2 = """The participants stated gender.
    The participant may decline to provide their gender."""
    string3 = "The distance the participant traveled."

    return pd.DataFrame({'variable_name': ['col1', 'col2', 'col3'],
                         'definition': [string1, string2, string3]})


def test_summary_statistics(input_data_frame):
    """Tests that the function returns summary statistics"""
    x = DataDocumenter(input_data_frame)
    x.summary_statistics()


def test_variable_names(input_data_frame, var_name_expected):
    """Tests that variable names are correctly created"""

    x = DataDocumenter(input_data_frame)

    var_name_mapping = {'col1': 'Age in years',
                        'col2': 'Gender',
                        'col3': 'Measure'
                        }

    x.variable_names(var_name_mapping)

    pd.testing.assert_frame_equal(var_name_expected, x.var_names)


def test_variable_definition(input_data_frame, var_definition_expected):
    """Tests that variable names are correctly created"""

    x = DataDocumenter(input_data_frame)
    def_string2 = """The participants stated gender.
    The participant may decline to provide their gender."""
    var_def_mapping = {'col1': 'The age of the participant when they joined',
                       'col2': def_string2,
                       'col3': 'The distance the participant traveled.'
                       }

    x.variable_definitions(var_def_mapping)

    pd.testing.assert_frame_equal(var_definition_expected, x.var_definitions)


def test_no_mapping_error(input_data_frame):
    """Tests no error is returned when all keys in the mapper are columns"""
    var_name_mapping = {'col1': 'Age in years',
                        'col2': 'Gender',
                        'col3': 'Measure'
                        }
    x = DataDocumenter(input_data_frame)

    x._validate_mappers(var_name_mapping)


def test_mapping_error(input_data_frame):
    """Tests error is returned when a key in the mapper is not a column"""
    var_name_mapping = {'col1': 'Age in years',
                        'col2': 'Gender',
                        'col100': 'Measure'
                        }

    x = DataDocumenter(input_data_frame)
    with pytest.raises(AssertionError):
        x._validate_mappers(var_name_mapping)
