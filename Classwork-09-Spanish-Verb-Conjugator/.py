# INPUT SECTION
user_verb = input("Enter a verb: ")
# PROCESSING SECTION
# Full list of subject pronouns we'll conjugate the verb for
pronouns = ['I', 'you', 'he/she', 'we', 'you all', 'they']

# Each verb type (-ar, -er, -ir) has its own set of endings
# stored as a list matching the order of pronouns above
endings_by_type = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# Strip the last 2 characters to get the root of the verb,
# and grab those last 2 characters to identify the verb type
verb_stem = user_verb[:-2]
verb_type = user_verb[-2:]

# Use the verb type as a key to retrieve the correct endings list
correct_endings = endings_by_type[verb_type]
