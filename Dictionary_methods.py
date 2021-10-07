#setdefault() method in dictionary

student = {"name": "Santhosh"}
rno = student.setdefault("rno.")
print("Student Details: ",student)
age = student.setdefault("age", 19)
print("Student Details(Final): ",student)

#fromkeys() method in dictionary

keys = {"Mangoes", "Strawberries", "Blackberries", "Bananas", "Blueberries"}
value = 'Fruits'
Fruits = dict.fromkeys(keys, value)
print("Fruits: ",Fruits)

#get() method in dictionary

University_Student = {"Name": "Santhosh", "age": 19}
print('Name: ', University_Student.get('Name'))
print('Age: ', University_Student.get('age'))
print("Fees: ", University_Student.get("Fees", 40000)) #We can provide value when not present

#values() when dicitonary is modified

Salaries = { "Shivnath": 200000000, "Ramnath": 300000000, "Somnath": 4000000000 }
values = Salaries.values()
print('Original items:', values)
del[Salaries["Ramnath"]] # deleting an item from dictionary
print('Updated items:', values)

#items() method in dictionary

sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.items())



