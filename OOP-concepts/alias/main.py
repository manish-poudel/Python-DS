# CONCEPTS: Alias, in programming, allows to identify the same object with different name.
# For example, assignment statement "foo == bar", creates an alias for the object bar where both identifier foo and bar
# refers to same object in the memory. Changing the attribute in one object will be reflected on the other object.


from student import Student

if __name__ == '__main__':

    student1 = Student("Manish", "Prolific")  # Create student object
    print(student1.name)  # OUTPUT: Manish
    print(student1.school)  # OUTPUT: Prolific

    # Create alias
    student2 = student1
    print(student2.name)    # OUTPUT: Manish
    print(student2.school)  # OUTPUT: Prolific

    # Change the attribute in student2
    student2.school = "KEHS"
    print(student2.school)  # OUTPUT: KEHS
    print(student1.school)  # OUTPUT: KEHS




