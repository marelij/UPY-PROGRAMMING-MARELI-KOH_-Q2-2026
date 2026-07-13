# Classwork #14: Error Handling

## Description
Three Python programs (Classwork #10, #11 and #12) were reworked to add proper
error handling. Each program validates user input and file access, catches
specific exceptions (`ValueError`, `KeyError`, `FileNotFoundError`, `OSError`,
`ImportError`, `ZeroDivisionError`, `IndexError`, `EOFError`,
`KeyboardInterrupt`), uses `try/except/finally` blocks, and prints clear error
messages instead of letting the program crash.

## Programs
- **school_management_system.py** (Classwork #10 – School Management System):
  Simulates a school login system with three roles (student, professor,
  coordinator). Validates login credentials, subject names and grade values,
  and recovers gracefully from invalid input instead of crashing.
- **mandelbrot_set_math.py** (Classwork #11 – The Mandelbrot Set): Reads grid
  parameters from `config.txt`, computes the number of iterations it takes
  each point to escape the Mandelbrot set, and writes the results to
  `clase.csv`. Handles a missing/malformed config file, missing keys, and
  file write errors.
- **mandelbrot_set_vis.py** (Classwork #12 – The Mandelbrot Set): Reads
  `config.txt` and `clase.csv`, converts the iteration counts into pixel
  colors, and saves the result as `mandelbrot-clase.png`. Handles a missing
  Pillow installation, missing/empty input files, malformed CSV rows, and
  image save errors.

## Features
- Input validation loops that keep asking for data until it is valid
  (username/password, subject, numeric grade between 0 and 10).
- `try/except/finally` structure: `finally` is used to make sure open files
  are always closed, even if an error occurs while reading or writing them.
- Specific exceptions are caught separately from generic ones, so the error
  message always tells the user what actually went wrong.
- The program structure follows the required `# INPUT`, `# PROCESS`, and
  `# OUTPUT` sections.

## How to run
Make sure you have Python 3 installed.

Clone this repository or download the source code:


git clone https://github.com/marelij/UPY-PROGRAMMING-MARELI-KOH_-Q2-2026.git


Go to the project folder:


cd Classwork-14-Error-Handling


Run any of the three programs:

python school_management_system.py   # Classwork #10
python mandelbrot_set_math.py        # Classwork #11
python mandelbrot_set_vis.py         # Classwork #12


Note: `mandelbrot_set_math.py` must be run before `mandelbrot_set_vis.py`,
since the visualization program reads the `clase.csv` file that the math
program generates. Both programs require a `config.txt` file in the same
folder.

## Environment and tools
- Language: Python 3.x
- Standard library only, plus [Pillow](https://pypi.org/project/Pillow/) for
  image generation in Classwork #12 (`pip install Pillow`)
- Version control: Git
- Hosting platform: GitHub

## AI use statement
AI (Claude) was used to write the code for the three programs, adding
`try/except/finally` blocks and specific exception handling on top of the
student's original working programs, as covered in class, and to write this
README file. All generated content was reviewed and tested to make sure it
meets the assignment's requirements.