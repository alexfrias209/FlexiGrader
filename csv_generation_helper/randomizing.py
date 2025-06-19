import pandas as pd
import numpy as np
import random

# This script checks each row's comments columns. If any comment column has a non-empty string, 
# it retains the corresponding criteria set. If all comments are empty, it randomly removes a set number of criteria 
# and shifts the remaining columns to the left.

random.seed(42)
np.random.seed(42)

def shift_criteria(df):
    col_prefixes = ['criteria{}_description', 'criteria{}_rating', 'student_score_{}', 'comments_{}']
    
    for idx in df.index:
        non_empty_criteria_numbers = []
        empty_criteria_numbers = []
        for num in range(1, 9):
            comment_col = 'comments_{}'.format(num)
            if not pd.isna(df.at[idx, comment_col]) and df.at[idx, comment_col] != '':
                non_empty_criteria_numbers.append(num)
            else:
                empty_criteria_numbers.append(num)
        
        if non_empty_criteria_numbers:
            criteria_numbers_to_remove = empty_criteria_numbers
        else:
            num_criteria_to_remove = random.randint(5, 7)
            criteria_numbers_to_remove = random.sample(range(1, 9), num_criteria_to_remove)
        
        criteria_numbers_to_remove.sort(reverse=True)
        
        for num in criteria_numbers_to_remove:
            for col_prefix in col_prefixes:
                df.at[idx, col_prefix.format(num)] = np.nan
        
        shift_count = 0  
        for num in range(1, 9):
            if num in criteria_numbers_to_remove:
                shift_count += 1  
            elif shift_count > 0:
                for col_prefix in col_prefixes:
                    new_col = col_prefix.format(num - shift_count)
                    old_col = col_prefix.format(num)
                    df.at[idx, new_col] = df.at[idx, old_col]
                    df.at[idx, old_col] = np.nan

    return df

file_path = 'EverythingCSV.csv'
df = pd.read_csv(file_path)

df_corrected = shift_criteria(df)

output_file_path = 'CommentsWithRandomizeNonCommentRows.csv'
df_corrected.to_csv(output_file_path, index=False)
