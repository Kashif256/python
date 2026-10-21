# dictonary

# dictonary is used to store in key- value pair. It is defined in {} brackets and it is separated by commas.

# values are mutable and can be changed but keys are immutable and cannot be changed.


student = {
    "name": "Kashif",
    "age": 21,
    "mark": 85
}
print(student) # o/p => {'name': 'Kashif', 'age': 21, 'mark': 85}
student["name"] = "sanu" # changing the value of keys from kashif to sanu
print(student)  # o/p => {'name': 'sanu', 'age': 21, 'mark': 85}
student["gender"] = "male" # adding new key and value pair
print(student)  # o/p => {'name': 'sanu', 'age': 21, 'mark': 85, 'gender': 'male'}
print(type(student))  # class 'dict'

# name, age, mark are keys and Kashif, 21, 85 are values.
