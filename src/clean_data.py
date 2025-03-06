import numpy as np 
import pandas as pd
import os 

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df.drop_duplicates()
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.replace(r"^\s*$", np.nan, regex=True)
    return df

def extract_data(df):
    df = df[['Country',
        'Age',
        'EdLevel',
        'DevType',
        'YearsCode',
        'YearsCodePro',
        'Employment',
        'ConvertedCompYearly',
        'JobSatPoints_6', 
        "JobSat",
        "Industry",
        "LanguageHaveWorkedWith",
        "DatabaseHaveWorkedWith",
        "PlatformHaveWorkedWith",
        "WebframeHaveWorkedWith",
        "AISearchDevHaveWorkedWith",
        "AISearchDevAdmired",
        "DatabaseAdmired",
        "LanguageAdmired",
        "PlatformAdmired", 
        "WebframeAdmired",
        "AIToolCurrently Using",
        "AISelect", 
        "AIBen",
        "AIThreat", 
        "AIComplex",
        "AIChallenges",
        "AIAcc"]]
    return df

def years_code_to_int(year):
    if pd.isnull(year):
        return np.nan
    if year == 'Less than 1 year':
        return "0-10 years"
    elif year == 'More than 50 years':
        return "50+ years"
    else:
        year = int(year)
        if year <= 2:
            return "0-2 years"
        elif year <= 5:
            return "2-5 years"
        elif year <= 10:
            return "5-10 years"
        elif year <= 20:
            return "10-20 years"
        elif year <= 30:
            return "20-30 years"
        elif year <= 40:
            return "30-40 years"
        elif year <= 50:
            return "40-50 years"
        else:
            return "50+ years"

def add_expyearspro_column(df):
    df['ExpYearsCodePro'] = df['YearsCodePro'].apply(years_code_to_int)
    return df

def update_csv(df, file_path,output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f'updated_{file_path}')
    df.to_csv(output_path, index=False)
    return output_path