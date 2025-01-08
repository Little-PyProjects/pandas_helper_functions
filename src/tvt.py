import pandas as pd
from sklearn.model_selection import train_test_split


def preprocess_data(
    df, target_col="total_sales_price", test_size=0.2, val_size=0.25, random_state=1
):
    """
    Preprocess the dataset by splitting it into training, validation, and test sets,
    and separating the target variable. Default is 60/20/20 split

    Parameters:
    df (pd.DataFrame): The input dataframe containing the dataset.
    target_col (str): The name of the target column. Default is 'y'.
    test_size (float): The proportion of the dataset to include in the test split. Default is 0.2.
    val_size (float): The proportion of the training set to include in the validation split. Default is 0.25.
    random_state (int): The random seed used for shuffling the data. Default is 42.

    Returns:
    tuple: A tuple containing:
        - df_train (pd.DataFrame): The training set with the target column removed.
        - df_val (pd.DataFrame): The validation set with the target column removed.
        - df_test (pd.DataFrame): The test set with the target column removed.
        - y_train (pd.Series): The target values for the training set.
        - y_val (pd.Series): The target values for the validation set.
        - y_test (pd.Series): The target values for the test set.
    """

    df_full_train, df_test = train_test_split(
        df, test_size=test_size, random_state=random_state
    )
    df_train, df_val = train_test_split(
        df_full_train, test_size=val_size, random_state=random_state
    )

    # Reset indices and separate target variable
    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    y_train = df_train.pop(target_col)
    y_val = df_val.pop(target_col)
    y_test = df_test.pop(target_col)

    return df_train, df_val, df_test, y_train, y_val, y_test


# Example usage:
# df_train, df_val, df_test, y_train, y_val, y_test = preprocess_data(df, target_col='jamb_score', random_state=1)

# Example usage:
# df_train, df_val, df_test, y_train, y_val, y_test = preprocess_data(df, target_col="total_sales_price", test_size=0.2, val_size=0.25, random_state=1)
