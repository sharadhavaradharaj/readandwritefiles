import csv

# Open the input file in read mode
input_file =  open('EmployeePay.csv', 'r') 
reader = csv.reader(input_file)
    
# Ignore the header row
next(reader)
    
# Loop over each row in the input file
for row in reader:
    # Extract the employee details from the row
    employee_id = row[0]
    employee_name = row[1]
    job_title = row[2]
    salary = row[3]
        
    # Print the details of the employee
    print(f"Employee ID: {employee_id}")
    print(f"Employee Name: {employee_name}")
    print(f"Job Title: {job_title}")
    print(f"Salary: {salary}\n")
    
#End of code
