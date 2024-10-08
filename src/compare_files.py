import filecmp
import pandas as pd


def compare_data(file1, file2, method=1, is_file_level=False):
    """
    Compare two datasets (or files) to determine if they are identical.

    Parameters:
    -----------
    file1 : str or pd.DataFrame
        The first file path or DataFrame to compare.
    file2 : str or pd.DataFrame
        The second file path or DataFrame to compare.
    method : int, optional
        Method to use for comparison:
        - 1 : DataFrame equality comparison (default).
        - 2 : Hash-based comparison (ignores row/column order).
        - 3 : Byte-level file comparison (includes file metadata).
    is_file_level : bool, optional
        If True, indicates that file-level byte comparison should be used (only valid with method 3).

    Returns:
    --------
    str
        A message indicating whether the two datasets or files are identical.

    Explanation of Methods:
    -----------------------
    1. **DataFrame Equality Comparison**:
       - Uses `pandas` to check if both DataFrames are equal.
       - Pros: Straightforward, checks data and structure.
       - Cons: Sensitive to row/column order.
       - Recommended when both data and structure matter.

    2. **Hash-Based Comparison**:
       - Sorts the DataFrames to ensure order does not matter, then compares their hashes.
       - Pros: Ignores row/column order, focuses on data equality.
       - Cons: Slower than simple comparison, requires additional sorting.
       - Recommended when you want to ensure data equality regardless of order.

    3. **Byte-Level File Comparison**:
       - Compares the raw binary contents of the files, including metadata.
       - Pros: Quick and exact comparison, checks file metadata and structure.
       - Cons: Doesn't account for logical equivalence (e.g., same data with different metadata).
       - Recommended when you need to ensure the files are byte-for-byte identical, including metadata.
    """

    if method == 3 and is_file_level:
        # Byte-level file comparison using filecmp
        are_identical = filecmp.cmp(file1, file2, shallow=False)
    else:
        # Assume DataFrame comparison for methods 1 and 2
        if not isinstance(file1, pd.DataFrame) or not isinstance(file2, pd.DataFrame):
            raise ValueError(
                "For methods 1 and 2, inputs must be pandas DataFrames.")

        if method == 1:
            are_identical = file1.equals(file2)
        elif method == 2:
            df1_hash = pd.util.hash_pandas_object(
                file1.sort_index(axis=1)).sum()
            df2_hash = pd.util.hash_pandas_object(
                file2.sort_index(axis=1)).sum()
            are_identical = df1_hash == df2_hash
        else:
            raise ValueError("Invalid method selected. Choose 1, 2, or 3.")

    return (
        "The two datasets/files are identical."
        if are_identical
        else "The two datasets/files are different."
    )

