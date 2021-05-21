"""Main module."""
import pandas as pd

class DataDocumenter():
    """Document Class"""

    def __init__(self, data_frame: pd.DataFrame) -> None:
        self.data_frame = data_frame
        pass

    def variable_definitions():
        pass

    def variable_names(self, name_mapping):
        """Assignes a meaningful name to the variables in the data frame."""
        # This maping gives better column names at the end of the process.
        final_column_names = {'index': 'variable_name', 0:'variable'}

        # Take the name mapping and create a data frame with a colum for the
        # name of the variable in the raw data and a column for the human
        # readable name.
        self.var_names = (pd.Series(name_mapping)
                          .to_frame()
                          .reset_index()
                          .rename(columns=final_column_names)
                         )

    def value_labels():
        pass

    def summary_statistics(self):
        numeric_describe = self.data_frame.describe()
        missing_counts = self.data_frame.isna().sum()

    def generate_dictionary():
        pass

    def _validate_mappers(self, mapper):
        column_names = self.data_frame.columns
        bad_key_error = """One or more keys provided in the mapping are
            not present in the data frame"""


        present_in_df = [i in column_names for i in mapper.keys()]

        assert all(present_in_df), bad_key_error
