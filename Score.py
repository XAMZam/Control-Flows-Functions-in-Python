def rate_performance(score):
    if score >= 80:
        return "Distiction"
    elif 60 <= 70:
        return "credit"
    elif 50 <=40:
        return "Fair"
    else :
        return "Fail"
    
score = int(input("Enter the student's score: "))

result = rate_performance(score)

print("Student's performance:", result)