
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# 1. Total score answer

# 1st option
total_score = 0
for score in student_scores : 
    total_score += score 
print(f"The total score is {total_score}.")

# 2nd option
print(f"The total score is {sum(student_scores)}.")

# 2. Highest score answer

# 1st option
max_score = 0
for score in student_scores : 
    if score >= max_score : 
        max_score = score

print(f"The highest score is {max_score}.")

# 2nd option
print(f"The highest score is {max(student_scores)}.")
