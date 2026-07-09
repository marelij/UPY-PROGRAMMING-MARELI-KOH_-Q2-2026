# Classwork #13 - Error Handling

## Description
Three Python programs (Classwork #07, #08, and #09) rebuilt to apply proper error handling. Each program validates user input in a loop, raises and catches specific exceptions (including custom ones), uses try/except/else/finally blocks, and logs warnings/errors to a .log file instead of letting the program crash.

## Programs

- *verifier_digit.py* (Classwork #07 – Verifier Digit): Calculates the verification digit of a UTFSM roll number, validating the roll format and catching mismatches with a custom DigitoVerificadorError.
- *numerical_integration.py* (Classwork #08 – Numerical Integration): Approximates the integral of a function chosen from a fixed list, using Default/Custom/Auto-adjust modes, and compares the result against the exact value (absolute and relative error).
- *spanish_verb_conjugator.py* (Classwork #09 – Spanish Verb Conjugator): Conjugates a regular Spanish verb (-ar/-er/-ir) in present tense for all six pronouns, validating the verb before processing it.

## Features
- Input validation loops that keep asking until the data is valid.
- Custom exceptions (DigitoVerificadorError, OpcionInvalidaError, IntervaloInvalidoError, TerminacionInvalidaError) that store extra details about the error.
- try/except/else/finally structure: else runs only when no error occurred, finally runs regardless.
- logging module writes warnings and errors (with timestamp and severity level) to a .log file.
- Program structure follows the required INPUT, PROCESS, and OUTPUT sections.

## How to Run
Make sure you have Python 3 installed.

Clone this repository or download the source code:


git clone https://github.com/marelij/UPY-PROGRAMMING-MARELI-KOH_-Q2-2026.git


Go to the project folder:


cd Classwork-13-Error-Handling


Run any of the three programs:


CW07.py      # Classwork #07
CW08.py # Classwork #08
CW09.py # Classwork #09


## Environment & Tools
- Language: Python 3.x
- Standard library only (logging, math)
- Version Control: Git
- Hosting Platform: GitHub

## AI Use Declaration
AI (Claude) was used to write the code for the three programs, applying try/except/else/finally, custom exceptions, and logging as covered in class, and to write this README. All generated content was reviewed and tested to ensure it met the assignment requirements
