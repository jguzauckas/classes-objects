# Create a function that takes in a name and a grade level
# and return a formatted string sentence that has both of
# those pieces of information (i.e., "Saad is in grade 12.")
def school(name: str, grade: int) -> str:
    return f"{name} is in grade {grade}."


# Call your function with two sets of information
school("Saad", 12)
school("Christina", 12)

# Create another function that takes in a name and a grade level
# and prints out a statement with both of those pieces of information
# (i.e., "Saad is in grade 12.")
def schoolprint(name: str, grade: int) -> None:
    print(f"{name} is in grade {grade}.")


# Call your function with two sets of information
schoolprint("Saad", 12)
schoolprint("Christina", 12)

# Create a function that takes in a boolean and a float. If the
# boolean is True, return the float times 2, and if the boolean
# is False, return the float divided by 2
def numchange(tf: bool, num: float) -> float:
    if tf:
        return num * 2
    else:
        return num / 2


# Call your function twice, once with a True and once with a False.
numchange(True, 2.5)
numchange(False, 5.2)
