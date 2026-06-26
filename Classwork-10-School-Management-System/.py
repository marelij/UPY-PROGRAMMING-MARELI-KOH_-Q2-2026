#Input
# Required Structures
users = {
    'jperez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo':	{
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':	{
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
while True:

    logged = False

    while logged == False:

        username = input("User: ")

        if username == "exit":
            exit()

        password = input("Password: ")

        if password == "exit":
            exit()

        if username in users:

            if users[username]["password"] == password:

                logged = True

                print()
                print(f"Welcome {users[username]['name']}")
                print(f"Role: {users[username]['rol']}")

            else:
                print()
                print("Incorrect password.")

        else:
            print()
            print("User not found.")

    role = users[username]["rol"]

    if role == "student":

        print()
        print("School Report")
        print(f"Student: {users[username]['name']}")

        approved = set()

        for subject in subjects:

            print(f"{subject}: {notes[username][subject]}")

            if notes[username][subject] >= 8:
                approved.add(subject)

        pending = set(subjects) - approved

        print()
        print(f"Approved Subjects: {approved}")
        print(f"Pending Subjects: {pending}")

        print()
        option = input("exit / continue: ")

        if option == "exit":
            exit()
        else:
            continue


    elif role == "professor":

        print()
        print("Students")

        for user in users:
            if users[user]["rol"] == "student":
                print(f"{user}: {users[user]['name']}")

        student = input("Student username: ")

        if student == "exit":
            exit()

        while student not in notes:
            print("Student not found.")
            student = input("Student username: ")

            if student == "exit":
                exit()

        print()
        print("Subjects")

        for subject in subjects:
            print(subject)

        subject = input("Subject: ")

        if subject == "exit":
            exit()

        while subject not in subjects:

            print("Invalid subject.")
            subject = input("Subject: ")

            if subject == "exit":
                exit()

        confirm = "no"

        while confirm != "yes":

            grade = input("New grade: ")

            if grade == "exit":
                exit()

            grade = float(grade)

            while grade < 0 or grade > 10:

                print("Grade must be between 0 and 10.")
                grade = input("New grade: ")

                if grade == "exit":
                    exit()

                grade = float(grade)

            old = notes[student][subject]

            print()
            print(f"{subject}: {old} ==> {grade}")

            confirm = input("Do you confirm? (yes/no): ")

            if confirm == "exit":
                exit()

            if confirm == "yes":
                notes[student][subject] = grade
                print("Grade updated.")
            else:
                print("Update cancelled.")

        print()
        option = input("exit / continue: ")

        if option == "exit":
            exit()
        else:
            continue


    elif role == "coordinator":

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
        option = input("exit / continue: ")

        if option == "exit":
            exit()
        else:
            continue