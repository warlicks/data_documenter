"""Main module."""
import pandas as pd


class DataDocumenter():
    """Document Class"""

    def __init__(self, data_frame: pd.DataFrame) -> None:
        self.data_frame = data_frame

    def variable_definitions(self, definition_mapping: dict):
        """Assigns a definition to each variable in the data frame"""
        self._validate_mappers(definition_mapping)
        final_column_names = {'index': 'variable_name', 0: 'definition'}
        self.var_definitions = self._mapping_to_df(definition_mapping,
                                                   final_column_names)

    def variable_names(self, name_mapping):
        """Assigns a meaningful name to the variables in the data frame."""
        # Check hat all columns in the mapping are in the data.
        self._validate_mappers(name_mapping)

        # This maping gives better column names at the end of the process.
        final_column_names = {'index': 'variable_name', 0: 'variable'}

        # Take the name mapping and create a data frame with a colum for the
        # name of the variable in the raw data and a column for the human
        # readable name.
        self.var_names = self._mapping_to_df(name_mapping, final_column_names)

    def value_labels():
        pass

    def summary_statistics(self):
        numeric_describe = self.data_frame.describe()
        missing_counts = self.data_frame.isna().sum()

    def generate_dictionary():
        pass

    def _validate_mappers(self, mapper):
        """Checks that all the keys in mapper dict are in the data frame.
        This is an internal method used to prevent errors when joining the data.
        Nothing is returned if all the keys are present in the data frame. It
        throws an assertion error if one or more of keys are not present in the
        data frame.

        It does not return an error if columns present in the data frame are not
        keys in the dictionary.

        Args:
          mapper: a dictionary where the keys are expected to be columns in the
            data frame.

        Returns: None

        Raises:
          AssertionError: One or more of the keys provided in the mapping are
            not present in the data frame.

        """
        column_names = self.data_frame.columns
        bad_key_error = """One or more keys provided in the mapping are
            not present in the data frame"""

        present_in_df = [i in column_names for i in mapper.keys()]

        assert all(present_in_df), bad_key_error

    def _mapping_to_df(self, mapper, final_column_names):
        """Converts the mapping dictionary to a data frame
        An internal function used whenever a dictionary is used to map metadata
        to the columns of the data frame.


        """
        return (pd.Series(mapper)
                .to_frame()
                .reset_index()
                .rename(columns=final_column_names)
                )
