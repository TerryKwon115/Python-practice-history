student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Total Score Calculation (Version 1)

total_score = 0
for score in student_scores : 
    total_score += score 
print(f"The total score is {total_score}.")

# Total Score Calculation (Version 2)

print(f"The total score is {sum(student_scores)}.")

# Highest Score Calculation (Version 1)

max_score = 0
for score in student_scores : 
    if score >= max_score : 
        max_score = score

print(f"The highest score is {max_score}.")

# Highest Score Calculation (Version 2)

print(f"The highest score is {max(student_scores)}.")
