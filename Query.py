import csv
import json

#holding the variables with respective names here
variables = ['id', 'name', 'lastname', 'email', 'grade']

#reading the csv file here
def csv_file_reader(filename = "students.csv"):
    data = []
    with open(filename, 'r') as file:
        csvreader = csv.reader(file, delimiter=';')
        for row in csvreader:
            data.append(row)
            
    return data

#sorting the given data in Ascending or Descending Order Based On reverse boolean(rev)
def sort_data(records,rev = False):
    func = lambda x: x[0]
    sorted_records = sorted(records, key=func,reverse=rev)
    return sorted_records

#Checking if the given Data's conditions fit with the method 
def check_conditions(data):
    if(len(data) != 5):
        print("Input is missing " + str(5-len(data)) + " values")
        return False
    else:
        try:
            num = int(data[0])
        except ValueError:
            print("First value of the input should be an integer, which represents student number")
            return False
        if not isinstance(data[1], str):
            print("Second value of the input should be an string, which represents student name")
            return False
        if not isinstance(data[2], str):
            print("Third value of the input should be an string, which represents student surname")
            return False
        if not isinstance(data[3], str):
            print("Fourth value of the input should be an string, which represents student mail")
            return False
        try:
            num = int(data[4])
        except ValueError:
            print("Last value of the input should be an integer, which represents student grade")
            return False
    
    return True


#Turning Input into operation from the list ([grade], [<], [40] will be converted as grade < 40)
#We're also taking a student data to perform the operation and get the result for that student data
def operand_handler(operation,data = []):
    check_value = -1
    for i in variables:
        if(operation[0] == i):
            check_value = variables.index(i)
    
    if(check_value == -1):
        print("column_name in operand is Invalid!")
        return False
    
    if(data[0] == 'id'):
        return False
    
    if operation[1] == '=':
        return data[check_value] == operation[2]
    elif operation[1] == '!=':
        return data[check_value] != operation[2]
    elif operation[1] == '<':
        return int(data[check_value]) < int(operation[2])
    elif operation[1] == '>':
        return int(data[check_value]) > int(operation[2])
    elif operation[1] == '<=':
        return int(data[check_value]) <= int(operation[2])
    elif operation[1] == '>=':
        return int(data[check_value]) >= int(operation[2])
    elif operation[1] == '!<':
        return int(data[check_value]) >= int(operation[2])
    elif operation[1] == '!>':
        return int(data[check_value]) <= int(operation[2])
    else:
        print("Operation is Invalid")
        
    return False

#We're handling the whole Select Operation Here
#We're using operand_handler() to perfom necessary comparisons
#We're also usinng the operand_handler() in combination to perform AND , OR operations
def select_operation_handler(one_operand, operation,data = []):
    selected_students = []
    if(one_operand):
        op = [(operation[2]),(operation[3]),(operation[4])]
        for student in data:
            if(operand_handler(op,student) == True):
                selected_students.append(student)
          
    else:
        op1 = [(operation[2]),(operation[3]),(operation[4])]
        op2 = [(operation[6]),(operation[7]),(operation[8])]
        
        if(operation[5] == 'AND'):
            for student in data:
                if(operand_handler(op1,student) & operand_handler(op2,student)):
                    selected_students.append(student)
        else:
            for student in data:
                if(operand_handler(op1,student) | operand_handler(op2,student)):
                    selected_students.append(student)    

    
    if(operation[len(operation)-1] == 'ASC'):
        selected_students = sort_data(selected_students)
    elif(operation[len(operation)-1] == 'DSC'):
        selected_students = sort_data(selected_students,True)
    else:
        print("The Sorting Preference isn't given! (ASC,DSC)")
    
    
    for student in selected_students:
        string = ""
        if(operation[1].__contains__('id')):
            string += student[0]
        if(operation[1].__contains__('name')):
            string += " " +student[1]
        if(operation[1].__contains__('lastname')):
            string += " " + student[2]
        if(operation[1].__contains__('email')):
            string += " " + student[3]
        if(operation[1].__contains__('grade')):
            string += " " + student[4]     
        if(operation[1].__contains__('ALL')):
            string =  student
        print(string) 
    
    
    print("Matching Students are succsessfully Selected!")

    return selected_students

#We're handling the whole Delete Operation Here
#We're using operand_handler() to perfom necessary comparisons
#We're also usinng the operand_handler() in combination to perform AND , OR operations
def delete_operation_handler(one_operand, operation,data = []):
    selected_students = []
    if(one_operand):
        op = [(operation[1]),(operation[2]),(operation[3])]
        for student in data:
            if(operand_handler(op,student) == True):
                    selected_students.append(student)
    else:
        op1 = [(operation[1]),(operation[2]),(operation[3])]
        op2 = [(operation[5]),(operation[6]),(operation[7])]
        
        if(operation[5] == 'AND'):
            for student in data:
                if(operand_handler(op1,student) & operand_handler(op2,student)):
                    selected_students.append(student)
        else:
            for student in data:
                if(operand_handler(op1,student) | operand_handler(op2,student)):
                   selected_students.append(student)
    
    for student in selected_students:
        data.remove(student)
        
    if(operation[len(operation)-1] == 'ASC'):
        data = sort_data(data)
    elif(operation[len(operation)-1] == 'DSC'):
        data = sort_data(data,True)
    else:
        print("The Sorting Preference isn't given! (ASC,DSC)")
    
    print("Matching Students are succsessfully Removed!")
    
    return data

#main Program is actually the core of the program, where we perform the input and get the results
def main_program():
    
    #Printing a cool welcome message
    print()
    print()
    print("+------------------------+----------------------------------------------------+")
    print("|  Input Field           |    Welcome to The Simple Database Query System     |")
    print("|                        |  Made By Edip Yekta Güler & Mustafa İzzet Yumuşak  |")
    print("+------------------------+----------------------------------------------------+")
    print()
    
    #setting the input varaible
    query = " "
    
    #taking the variable into the loop until EXIT keyword is given
    while (query != "EXIT"):
        #Getting the first input
        query = input("Please enter Operation ->")
        #Checking the input, splitting it and replacing unnececarry parts from it to perform whats asked in the input
        
        if(query[:26].upper() == 'INSERT INTO STUDENT VALUES'):
            query = query.replace('INSERT INTO STUDENT VALUES(', '')
            query = query.replace(')', '')
            query_list = query.split(',')
            if(check_conditions(query_list)):
                data.append(query_list)
                print("Insert Operation is Suceessfully Complete!")
            else:
                print("An Error Occured! Please Try Again")      
        
        elif(query.__contains__("FROM STUDENTS WHERE")):
            
            query = query.replace(' FROM STUDENTS WHERE', '')
            query = query.replace(' ORDER BY', '')
            query = query.replace('‘','')
            query = query.replace('’','')
            one_operand = True
            if(query.__contains__("AND") | query.__contains__("OR")):
                one_operand = False
                
            operation = query.split(' ')
            
            if(operation[0] == 'SELECT'):
                data = select_operation_handler(one_operand,operation,data)
            elif(operation[0] == 'DELETE'):
                data = delete_operation_handler(one_operand, operation,data)
            else:
                print('Error! No valid operation type is given')
                
        elif(query == "EXIT"):
            print("EXIT operation is successfully handled")
            print("Writing Results to JSON data...")
            
        else:
            print("Input is Invalid")
    
    return data #returning the data at the end

#starting the main program
all_data = main_program()

#Writing to Json File
file_path = "data.json"
with open(file_path, 'w') as json_file:
    json.dump(all_data, json_file)
print("JSON file created successfully.")
