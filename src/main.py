from clean_data import clean_data, extract_data, add_expyearspro_column, update_csv
from split_data import load_data, transform_data, save_data

def main(file_path, output_dir):
    df_cleaned = clean_data(file_path)
    df_extracted = extract_data(df_cleaned)
    add_cols_expyearspro = add_expyearspro_column(df_extracted)
    update_file_path = update_csv(add_cols_expyearspro, file_path, output_dir)
    df = load_data(update_file_path)
    processed_data = transform_data(df)
    save_data(processed_data, output_dir)

if __name__ == "__main__":
    file_path = "survey_results_public.csv"
    output_dir = "data"
    main(file_path, output_dir)
