# Pandas Helper Functions

Currently this contains I two files with functions that are useful.

# `pandas_helpers.py`




## Data familiarization
- all_uniques_in_all_cols(df)
- nulls_in_col(df, col, count:int)
- rows_w_col_val(df, col, val)
- sum_two_columns(dataframe, col1, col2)

## dealing with NaNs

### simple_nan_overwrite(df, 'nancol', 'repcol'):
    """
    usage: For each NaN value found, it takes the value from the same row in the `repcol` column and uses it to replace the NaN value in `nancol`.

    out: After filling the NaN values, returns the now filled `nancol`.  `repcol` column is then removed from the DataFrame.

    This is functionally the same as the following SQL:

    UPDATE my_table
    SET nancol = COALESCE(nancol, repcol);

    """
  




### complex_nan_overwrite(df, 'nan_col', 'fill_1', 'fill_2', 'remainders'):
    """
    replace NaN values in a column with values of a second column,
    will optinally replace with optional third column if both are missing,
    and optionally replace with a default if all three are missing

    """





## Converting data


## Geo Cordinates
### splitLatLong(df):
    Takes a single combined latitude/longitude position, breaks into two columns, and gets rid of the old column.



### dms2dd(field):
    Converts postition from Degrees, Minutes, Seconds (DMS) to decimal degrees.

### conv_to_dd(df):
    Sends latitude and longitude columns to dms2dd function for conversion to decimal degrees.



## Modeling data
- get_features_and_target


# `compare_files`
Compares two dataframes with options for:
  - dataframe level
  - hash level
  - byte level