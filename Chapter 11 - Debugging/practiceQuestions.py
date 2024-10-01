# Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.


# Question 1: Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
# spam = 5
# assert not spam < 10, "spam is less than 10"


# Question 2: Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
# bacon = "hello"
# eggs = "help"

# assert bacon.lower() != eggs.lower(), "Bacon should not be the same as eggs."

# Question 3: Write an assert statement that always triggers an AssertionError
# assert False, "This should always trigger an AssertionError."
