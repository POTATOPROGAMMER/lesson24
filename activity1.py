print("dictionaries and its types.....")
student_dict={"name":"zayed","age":11,"grade":"6th"}
print(student_dict)
print("length:",len(student_dict))
print(student_dict["name"])
print(student_dict["age"])
print(student_dict["grade"])
student_dict["age"]=11
print(student_dict)
student_dict["gender"]="male"
print(student_dict)
del student_dict["grade"]
print(student_dict)
print("keys:",student_dict.keys())
print("values:",student_dict.keys())
print("items:",student_dict.keys())
student_dict.clear()
print(student_dict)

