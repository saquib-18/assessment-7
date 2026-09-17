# generate_exam_report.py
with open("exam_report.txt", "w") as f:
    f.write("=========================================\n")
    f.write("ONLINE EXAMINATION & EVALUATION SYSTEM\n")
    f.write("=========================================\n")
    f.write("Exam Title: Midterm Python Programming\n")
    f.write("Total Students Evaluated: 150\n")
    f.write("Passed: 135\n")
    f.write("Failed: 15\n")
    f.write("Average Score: 82.5%\n")
    f.write("=========================================\n")
    f.write("Status: Report successfully generated.\n")

print("Exam evaluation report created successfully.")
