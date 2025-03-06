import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

# Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Identify columns containing multiple values
def find_category_columns(df):
    return [col for col in df.columns if df[col].astype(str).str.contains(";").any()]

# Check if column exists in dataframe
def check_column(df, column_name):
    return column_name in df.columns

# Split, explode and clean data
def split_and_explode(df, column_name):
    if not check_column(df, column_name):
        logging.error(f"Error: '{column_name}' column not found.")
        return pd.DataFrame(columns=[column_name])

    missing_value = df[column_name].isnull().sum()
    if missing_value > 0:
        logging.warning(f"Warning: '{column_name}' column has {missing_value} missing values.")
    
    df = df.dropna(subset=[column_name]).copy()
    df.loc[:, column_name] = df[column_name].astype(str).str.split(';')
    return df.explode(column_name)

# Transform data
def transform_data(df):
    category_columns = find_category_columns(df)  
    logging.info(f"Detected category columns: {category_columns}")

    processed_data = {}
    
    for column in category_columns:
        df_exploded = split_and_explode(df, column)
        if not df_exploded.empty:
            top10 = df_exploded[column].value_counts().head(10).index
            df_exploded = df_exploded[df_exploded[column].isin(top10)]
            processed_data[column.lower()] = df_exploded[[column]].reset_index(drop=True)

    return processed_data

# Save to CSV
def save_data(dfs, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for name, df in dfs.items():
        output_path = f"{output_dir}/{name}.csv"
        df.to_csv(output_path, index=False)
        print(f"Saved: {output_path}")

