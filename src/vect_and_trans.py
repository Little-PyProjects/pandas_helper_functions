from sklearn.feature_extraction import DictVectorizer

def transform_data(df_train, df_val):
    """
    Transform the training and validation data using DictVectorizer.

    Parameters:
    df_train (pd.DataFrame): The training set.
    df_val (pd.DataFrame): The validation set.

    Returns:
    tuple: A tuple containing:
        - dv (DictVectorizer): The fitted DictVectorizer.
        - X_train (csr_matrix): The transformed training set.
        - X_val (csr_matrix): The transformed validation set.
    """
    dv = DictVectorizer(sparse=True)
    X_train = dv.fit_transform(df_train.to_dict(orient='records'))
    X_val = dv.transform(df_val.to_dict(orient='records'))
    
    return dv, X_train, X_val
