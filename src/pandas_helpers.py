import pandas as pd
import os


def all_uniques_in_all_cols(df):
    '''
    use: lists all the unique values for evey column in a dataframe
    input: dataframe
    output: formatted output of all the unique values in the dataframe
    
    '''
    for col in df.columns.to_list():
        print(f"""There are {df[col].nunique()} unique values for {col}:
              {df[col].unique()}
              """)


def nulls_in_col(df, col, count:int):
    '''
    use: makes a dataframe showing the rows with null in particular column
    input: dataframe, 'single column', max rows to return
    output: dataframe of rows <= count with nulls in col 
    
    '''
    return df[df[col].isnull()].head(count)


def rows_w_col_val(df, col, val):
    '''
    use: makes a dataframe showing rows with particular in a specified column
    input: dataframe, 'single column', 'value to search'
    output: dataframe of rows <= count with nulls in col 
    
    '''
    return df.loc[df[col] == val]   


def sum_two_columns(dataframe, col1, col2):
    in: a dataframe and the name of two columns as parameters
    out: returns the sum of those columns.
    pass


def get_features_and_target(da): 
    ''' 
    return the features X and target y from a dataframe as NumPy arrays,
    so that we could use them in a machine learning algorithm.
    (The target will be a single column in your dataframe, and 
    features will be all other columns.) Think about what parameters
    you’ll need to accept in order to accomplish this, and what you’ll
    need to return.
    '''
    pass
