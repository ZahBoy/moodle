mathSYM = 0
pythonSYM = 0
englishSYM = 0
student_count = 0

best_student = ""
best_average = -1

with open("students.csv", "r", encoding="utf-8") as f:
    next(f)
    for line in f:
        line = line.strip()
        name, math_gr, python_gr, english_gr = line.split(",")
        math_gr = float(math_gr)
        python_gr = float(python_gr)
        english_gr = float(english_gr)

        mathSYM += math_gr
        pythonSYM += python_gr
        englishSYM += english_gr
        student_count += 1

        stud_average = (mathSYM + pythonSYM + englishSYM) / 3
        if stud_average > best_average:
            best_average = stud_average
            best_student = name

math_avg = mathSYM / student_count
python_avg = pythonSYM / student_count
english_avg = englishSYM / student_count

result = (
    "Середній бал по класу:"
    f"math: {math_avg}"
    f"python: {python_avg}"
    f"english: {english_avg}"
    ""
    f"Найкращий студент: {best_student} ({best_average})"
)

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result + "\n")

print(result)
