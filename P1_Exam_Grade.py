print("This code calculates the avaerage of all the grades scored in a exam.\n")

total_exams = int(input("Enter the total nummber of exams:\n"))
total_credits = int(input("Enter the total credits covered by these exams:\n"))

avg = 0

for i in range(total_exams):
    exam_score = int(input("Enter the marks scored in the exam:\n"))
    exam_credit = int(input("Enter the credits covered by this exam:\n"))

    avg = avg + exam_score * exam_credit / total_credits
print(f"Your total average is {avg}.")