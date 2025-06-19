import pandas as pd
import numpy as np


df = pd.read_csv('name.csv')

good = [
    "Great job! effectively solves the criteria",
    "Well done! Showcases your proficiency.",
    "Keep up the great work!",
    "Fantastic job! Your work is a model example for this criteria.",
    "Excellent job on meeting all the requirements.",
    "Great work! Your understanding of the concepts is very strong.",
    "Your work demonstrates a comprehensive understanding of the criteria.",
    "Excellent effort! Your skills are developing nicely.",
    "Keep pushing yourself! Your potential is evident in your work.",
    "Effective. Excellent job!",
    "Outstanding. Keep it up!",
    "Impressive work! You met the expectations of this criteria."
    "Your implementation works great!",
    "Great job on passing the criteria!",
    "Your work is a great example of good quality standards in this criteria.",
    "Excellent job in passing the criteria!",
    "Your work is exemplary and sets a high standard.",
    "Keep up the good work!",
    "You've demonstrated great understanding and execution of the criteria",
    "Well done! Your coding abilities are continuously improving.",
    "Great attention to detail! Your careful work is paying off.", ##
]

okay = [
    "Good attempt! You covered some points, but there's room for improvement.", 
    "You made a solid effort. but need more work.",
    "You have made some progress, but there are still some ways to improve.", 
    "Take another look at the requirements and ensure all are met in your code.", 
]

bad = [
    "Unfortunately, your code did not meet the criteria. I recommend revisiting the concepts and reworking your solution.",
    "Make sure you understand the criteria requirements fully before starting to code.",
]

good2, okay2, bad2 = [], [], []

good_count, okay_count, bad_count = 0, 0, 0

def get_feedback(feedback_list, backup_list, count):
    if not feedback_list:
        feedback_list.extend(backup_list)
        backup_list.clear()
    feedback = feedback_list.pop(0)
    backup_list.append(feedback)
    count += 1
    return feedback, count

def provide_feedback(max_score, student_score, comment):
    global good_count, okay_count, bad_count
    if pd.isna(comment):
        if student_score == max_score:
            feedback, good_count = get_feedback(good, good2, good_count)
            return feedback
        elif student_score > 0:
            feedback, okay_count = get_feedback(okay, okay2, okay_count)
            return feedback
        elif student_score == 0:
            feedback, bad_count = get_feedback(bad, bad2, bad_count)
            return feedback
    return comment

for index, row in df.iterrows():
    col_index = 1
    while True:
        criteria_total_col = f'criteria{col_index}_total'
        student_score_col = f'student_score_{col_index}'
        comment_col = f'comments_{col_index}'
        
        if pd.notna(row.get(criteria_total_col)):
            max_score = row[criteria_total_col]
            student_score = row[student_score_col]
            comment = row[comment_col]
            
            df.at[index, comment_col] = provide_feedback(max_score, student_score, comment)
        else:
            break
        col_index += 1

df.to_csv('234.csv', index=False)

print(f"Good feedback used: {good_count}")
print(f"Okay feedback used: {okay_count}")
print(f"Bad feedback used: {bad_count}")
