# INPUT
# Fixed data: users (login credentials), subjects (fixed list),
# and notes (grades per student per subject).
users = {
    'jperez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo': {
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez': {
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc': {
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam': {
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo': {
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa': {
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# PROCESS
# Main loop: handles login, then branches into the menu for the
# logged-in role (student / professor / coordinator).
while True:

    try:

        logged = False

        while logged == False:

            # INPUT
            username = input("User: ")

            if username == "exit":
                exit()

            # INPUT
            password = input("Password: ")

            if password == "exit":
                exit()

            # PROCESS - validate credentials against the users dictionary
            if username in users:

                if users[username]["password"] == password:

                    logged = True

                    # OUTPUT
                    print()
                    print(f"Welcome {users[username]['name']}")
                    print(f"Role: {users[username]['rol']}")

                else:
                    # OUTPUT
                    print()
                    print("Incorrect password.")

            else:
                # OUTPUT
                print()
                print("User not found.")

        role = users[username]["rol"]

        if role == "student":

            # OUTPUT
            print()
            print("School Report")
            print(f"Student: {users[username]['name']}")

            approved = set()

            # PROCESS - build approved/pending sets from notes
            for subject in subjects:

                # OUTPUT
                print(f"{subject}: {notes[username][subject]}")

                if notes[username][subject] >= 8:
                    approved.add(subject)

            pending = set(subjects) - approved

            # OUTPUT
            print()
            print(f"Approved Subjects: {approved}")
            print(f"Pending Subjects: {pending}")

            print()
            # INPUT
            option = input("exit / continue: ")

            if option == "exit":
                exit()
            else:
                continue

        elif role == "professor":

            # OUTPUT
            print()
            print("Students")

            for user in users:
                if users[user]["rol"] == "student":
                    print(f"{user}: {users[user]['name']}")

            # INPUT
            student = input("Student username: ")

            if student == "exit":
                exit()

            while student not in notes:
                print("Student not found.")
                # INPUT
                student = input("Student username: ")

                if student == "exit":
                    exit()

            # OUTPUT
            print()
            print("Subjects")

            for subject in subjects:
                print(subject)

            # INPUT
            subject = input("Subject: ")

            if subject == "exit":
                exit()

            while subject not in subjects:

                print("Invalid subject.")
                # INPUT
                subject = input("Subject: ")

                if subject == "exit":
                    exit()

            confirm = "no"

            while confirm != "yes":

                # INPUT
                grade = input("New grade: ")

                if grade == "exit":
                    exit()

                # PROCESS - validate the grade is numeric
                try:
                    grade = float(grade)
                except ValueError:
                    print("Invalid grade. Please enter a number.")
                    continue

                while grade < 0 or grade > 10:

                    print("Grade must be between 0 and 10.")
                    # INPUT
                    grade = input("New grade: ")

                    if grade == "exit":
                        exit()

                    try:
                        grade = float(grade)
                    except ValueError:
                        print("Invalid grade. Please enter a number.")
                        grade = -1  # forces the while loop to ask again

                old = notes[student][subject]

                # OUTPUT
                print()
                print(f"{subject}: {old} ==> {grade}")

                # INPUT
                confirm = input("Do you confirm? (yes/no): ")

                if confirm == "exit":
                    exit()

                # PROCESS - apply the update
                if confirm == "yes":
                    notes[student][subject] = grade
                    # OUTPUT
                    print("Grade updated.")
                else:
                    # OUTPUT
                    print("Update cancelled.")

            print()
            # INPUT
            option = input("exit / continue: ")

            if option == "exit":
                exit()
            else:
                continue

        elif role == "coordinator":

            # OUTPUT
            print()
            print("Coordinator Menu")

            print()
            print("Teachers:")

            for user in users:
                if users[user]["rol"] == "professor":
                    print(f"{user}: {users[user]['name']}")

            print()
            print("Subjects:")

            for subject in subjects:
                print(subject)

            print()
            print("Students Grades:")

            for student in notes:

                print()
                print(f"{users[student]['name']} ({student})")

                for subject in subjects:
                    print(f"{subject}: {notes[student][subject]}")

            print()
            # INPUT
            option = input("exit / continue: ")

            if option == "exit":
                exit()
            else:
                continue

    except KeyError:
        # OUTPUT
        print()
        print("A required key was not found. Returning to login.")
        continue

    except (EOFError, KeyboardInterrupt):
        # OUTPUT
        print()
        print("Program interrupted by the user.")
        exit()

    except Exception as e:
        # OUTPUT
        print()
        print(f"Unexpected error: {e}")
        continue

# OUTPUT
# The output of this program is printed directly to the console
# via the print() calls above (login result, school report,
# grade updates and the coordinator's read-only report).