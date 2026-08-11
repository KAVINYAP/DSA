def search_employee_id(emplist, key, index=0):
   
    if index >= len(emplist):
        return -1
    
    if emplist[index] == key:
        return index
    
    return search_employee_id(emplist, key, index + 1)

employee_database = ["EMP101", "EMP102", "EMP103", "EMP104", "EMP105"]
n=1
while n>0:
    user_input = input("Enter the Employee ID you want to search for: ")

    result_index = search_employee_id(employee_database, user_input)
    

    if result_index != -1:
        print(f"Success: Employee ID '{user_input}' was found at index {result_index}.")
    else:
        print(f"Not Found: Employee ID '{user_input}' does not exist in the database.")
