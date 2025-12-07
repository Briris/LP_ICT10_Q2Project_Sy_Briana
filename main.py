from pyscript import display

# Step 1: Store subject names in a tuple (since they don't change)
subjects = ("Science", "English", "ICT", "Math", "Filipino", "PE")

def get_grade(*args, **kwargs):
    grades = []

    # Step 2: Get grades directly from JavaScript using js.document
    from js import document

    # Get first name and last name
    firstname = document.getElementById("firstname").value
    lastname = document.getElementById("lastname").value

    for subject in subjects:
        grade_str = document.getElementById(subject.lower()).value
        try:
            grade = float(grade_str)
        except ValueError:
            display(f"⚠️ Invalid input. Please enter a number.", target="titleresults")
            return
        grades.append(grade)

    # Step 3: Compute the average
    average = sum(grades) / len(grades)

    # Step 4: Display results
    display(f"{firstname} {lastname}, your grades are:" , target="nameresults")
    for subject, grade in zip(subjects, grades):
        display(f"{subject}: {grade}" , target="results")
    display(f"Your \ngeneral average is {average:.2f}" , target="results")