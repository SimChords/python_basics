# This short program is used to determine if applicants meet the criteria for a Software Development Skills program.


# First pre_qualification criteria, is to check if the applicant did PURE MATHEMATICS or MATHEMATICS LITERACY.
mathematics = int(input("Which type of Maths did you do in matirc:\n1. Pure Maths or 2. Maths Literacy ?\n "))
if mathematics == 1:
    print("You may proceed with the application.\n")
if mathematics == 2:
    print('Sorry, we want candidates with pure maths.')
    exit()

'#'The first part asks the user to enter their year of birth and then it uses it to calculate their age todetermine whether they qualify.
birth_year = int(input("enter the year you were born: "))
applicant_age = 2024 - birth_year

# An if statement is used to determine if user can proceed to the next phase or not.
if applicant_age < 18:
    print(" You're too young for this program.")
    exit()
if applicant_age >= 18 and applicant_age <= 28:
    print("You're ",applicant_age, "years old. You can proceed with the application.\n")

# This part of the program asks the user to enter their marks/grades to determine if they meet the minimum requirements.
english_marks = round(float(input("Enter your English marks: ")),2)
print(f'You got {english_marks} {"%"} for English')
maths_marks = round(float(input("Enter your mathematics marks: ")),2)
print(f'You got {maths_marks} {"%"} for English')

if english_marks >= 50 and maths_marks >= 50:
    print("Congratulations, based on our selection criteria, you qualify for the program.")
    print("Please forward your CV and other relevant documents to the following email address: Jonedoe@xtsmail.org")
else:
    print ("Unfortunately, you do not qualify for the program.")