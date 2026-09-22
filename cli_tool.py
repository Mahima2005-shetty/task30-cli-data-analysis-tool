import argparse
import sys
import pandas as pd


def load_data(file_path):
    """Load CSV data and handle file-related errors."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        sys.exit(1)
    except pd.errors.ParserError:
        print("Error: Unable to parse the CSV file.")
        sys.exit(1)


def validate_columns(df, required_columns=None):
    """Validate that required columns exist in the dataset."""
    if required_columns:
        missing_columns = [
            column for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            print(
                "Error: Column(s) not found: "
                + ", ".join(missing_columns)
            )
            print("\nAvailable columns:")
            print(", ".join(df.columns))
            sys.exit(1)


def show_summary(df):
    """Display a general summary of the dataset."""
    print("\n" + "=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names:")
    for column in df.columns:
        print(f"- {column}")

    print("\nData Types:")
    print(df.dtypes.to_string())

    print("\nMissing Values:")
    print(df.isnull().sum().to_string())


def filter_data(df, column, operator, value):
    """Filter data using a selected column and comparison operator."""
    validate_columns(df, [column])

    try:
        if pd.api.types.is_numeric_dtype(df[column]):
            value = float(value)

        if operator == ">":
            result = df[df[column] > value]
        elif operator == "<":
            result = df[df[column] < value]
        elif operator == ">=":
            result = df[df[column] >= value]
        elif operator == "<=":
            result = df[df[column] <= value]
        elif operator == "==":
            result = df[df[column] == value]
        elif operator == "!=":
            result = df[df[column] != value]
        else:
            print(f"Error: Unsupported operator: {operator}")
            sys.exit(1)

        print("\n" + "=" * 60)
        print("FILTERED DATA")
        print("=" * 60)

        if result.empty:
            print("No matching records found.")
        else:
            print(result.to_string(index=False))
            print(f"\nMatching records: {len(result)}")

    except ValueError:
        print(
            f"Error: Invalid value '{value}' "
            f"for column '{column}'."
        )
        sys.exit(1)


def group_data(df, column):
    """Group data and display count and numeric averages."""
    validate_columns(df, [column])

    print("\n" + "=" * 60)
    print(f"GROUPED ANALYSIS BY: {column}")
    print("=" * 60)

    grouped_count = df.groupby(column).size().reset_index(name="count")

    print("\nRecord Count:")
    print(grouped_count.to_string(index=False))

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if numeric_columns:
        print("\nNumeric Averages:")
        grouped_average = df.groupby(column)[numeric_columns].mean()
        print(grouped_average.round(2).to_string())
    else:
        print("\nNo numeric columns available for average calculation.")


def show_statistics(df):
    """Display descriptive statistics for numeric columns."""
    print("\n" + "=" * 60)
    print("STATISTICAL REPORT")
    print("=" * 60)

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        print("No numeric columns available.")
        return

    print("\nDescriptive Statistics:")
    print(numeric_df.describe().round(2).to_string())


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Command-Line Data Analysis Tool - "
            "Analyze CSV datasets using Pandas."
        )
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to the CSV file to analyze."
    )

    parser.add_argument(
        "--summary",
        action="store_true",
        help="Display dataset summary and column information."
    )

    parser.add_argument(
        "--filter-column",
        help="Column name to use for filtering."
    )

    parser.add_argument(
        "--operator",
        choices=[">", "<", ">=", "<=", "==", "!="],
        help="Comparison operator for filtering."
    )

    parser.add_argument(
        "--value",
        help="Value to compare against when filtering."
    )

    parser.add_argument(
        "--group",
        help="Column name to group the data by."
    )

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Display statistical information for numeric columns."
    )

    args = parser.parse_args()

    # Load dataset
    df = load_data(args.file)

    # Validate that dataset contains columns
    if df.empty:
        print("Error: The dataset contains no records.")
        sys.exit(1)

    print(f"\nSuccessfully loaded: {args.file}")

    # Summary
    if args.summary:
        show_summary(df)

    # Filtering
    filter_arguments = [
        args.filter_column,
        args.operator,
        args.value
    ]

    if any(item is not None for item in filter_arguments):
        if not all(item is not None for item in filter_arguments):
            print(
                "\nError: Filtering requires all three options:"
                " --filter-column, --operator and --value"
            )
            sys.exit(1)

        filter_data(
            df,
            args.filter_column,
            args.operator,
            args.value
        )

    # Grouping
    if args.group:
        group_data(df, args.group)

    # Statistics
    if args.stats:
        show_statistics(df)

    # If no analysis option was selected
    analysis_selected = (
        args.summary
        or args.group
        or args.stats
        or any(item is not None for item in filter_arguments)
    )

    if not analysis_selected:
        print("\nNo analysis option selected.")
        print("Use --help to view available commands.")


if __name__ == "__main__":
    main()