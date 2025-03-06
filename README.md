# Stack Overflow 2024 Survey Analysis

The Stack Overflow 2024 Developer Survey dataset (https://survey.stackoverflow.co/) contains responses from 65,437 developers worldwide (consisting of 65,437 rows and 114 columns). The analysis is conducted through 4 dashboards (https://lookerstudio.google.com/reporting/77e60f7f-d0a2-461a-91dc-6bcfd5e741cb), focusing on technology preferences, participants' perspectives on AI, and demographics.

To ensure a structured analysis, I perform data cleaning, transformation, and categorization into distinct groups to extract meaningful insights enabling better visualization and decision-making.

## Data Processing Workflow ##

**1. Data Cleaning (clean_data.py)**

The first step involves cleaning the raw survey data to ensure consistency and usability. This includes:

- Removing Duplicates
- Removing unnecessary whitespace in text-based responses.
- Handling Missing Values: replacing empty strings with NaN to standardize missing data representation.
- After cleaning, specific columns are extracted to focus on key areas such as demographics, technology preferences.

***Key Functions***
- clean_data(file_path): Cleans the dataset by removing duplicates, trimming strings, and handling missing values.
- extract_data(df): Selects relevant columns for analysis, including country, job role, years of experience, technologies used, AI opinions, and job satisfaction.
- add_expyearspro_column(df): Categorizes professional coding experience into meaningful groups (e.g., "0-2 years", "10-20 years", etc.).
- update_csv(df, file_path, output_dir): Saves the cleaned and transformed data as a new CSV file.

**2. Data Transformation (split_data.py)**

Since some survey responses contain multiple values separated by semicolons (preferred programming languages...), we need to split and restructure them for analysis.

***Key Processes***
- Identifies columns where responses contain multiple values.
- Converts multi-value responses into separate rows for better analysis.
- Retains only the most frequently mentioned responses to focus on relevant insights.

***Key Functions***
- find_category_columns(df): Identifies columns with multiple values.
- split_and_explode(df, column_name): Splits semicolon-separated values and expands them into individual rows.
- transform_data(df): Applies the transformation to all detected multi-value columns.
- save_data(dfs, output_dir): Saves the processed data into separate CSV files.

**3. Main Execution Script (main.py)**

This script orchestrates the entire data processing workflow by:
- Cleaning and extracting relevant data
- Adding experience categories
- Updating and saving the cleaned dataset
- Transforming multi-value columns
- Saving structured data for further analysis

***Execution Steps:***

To run the full pipeline: 
```sh
python main.py
```
This will process the dataset and generate cleaned CSV files in the data directory.

**System Requirements**
- Python
- pandas
- numpy
- os
- logging

## Outputs and Usage ##
The cleaned and transformed dataset is stored in multiple CSV files, structured for dashboard visualizations and analysis.

## Dashboard ##
![Current Technology usage](/dashboard/current%20technology%20usage.png)

![Future Technology Trend](/dashboard/future%20technology%20trend.png)

![Participants' perspectives on AI](/dashboard/AI%20Trends.png)

!['Demographics](/dashboard/Demographics.png)
