# CONCEPTS: Copying allows to create a copy of an object where we can modify original or copied object in
# an independent manner. There are two ways to copy the object:

# SHALLOW COPY: This allows to create a separate copy of an object but the content will still be an alias to original.
# For eg, if we have a list of Person, then copying will allow to insert or delete in new object
# without affecting the original list but modifying the person in the list will be reflected on the original.

# DEEP COPY: This allows to create a copy of an object where inserting, deleting and even modifying in a copied object
# won't impact the original object.


from person import Person
import copy

if __name__ == '__main__':
    original_list_of_person = [Person("Manish", "Nepal"), Person("Ashwin", "Australia")]

    # Lets print the content
    print(original_list_of_person[0].name)  # Manish
    print(original_list_of_person[0].address)  # Nepal

    print(original_list_of_person[1].name)  # Ashwin
    print(original_list_of_person[1].address)  # Australia

    # Let's create a shallow copy first. That can be done using built in method called list

    shallow_copy = list(original_list_of_person)

    # Let's add one more person to the list and compare the length

    shallow_copy.append(Person("John", "USA"))
    print(len(shallow_copy))  # 3
    print(len(original_list_of_person))  # 2

    # So, adding the element on shallow copy list didn't add on the original list but what about modifying the content?

    shallow_copy[0].name = "Peter"

    print(shallow_copy[0].name)  # Peter
    print(original_list_of_person[0].name)  # Peter

    # It changed the name on the both list. So, what can be done then to prevent the modification in one list to
    # impact the content on original list. Python has built in class copy with built in function for shallow copy and
    # deep copy

    # Let's bring back the original name
    original_list_of_person[0].name = "Manish"

    deep_copy = copy.deepcopy(original_list_of_person)
    print(deep_copy[0].name)  # Manish
    print(original_list_of_person[0].name)  # Manish

    # Let's change the content now

    deep_copy[0].name = "Deep"
    print(deep_copy[0].name)  # Deep
    print(original_list_of_person[0].name)  # Manish


