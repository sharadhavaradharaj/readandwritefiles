import csv

# Open the input file in read mode
input_file = open('customers.csv', 'r') 

reader = csv.reader(input_file , delimiter=',')

# Ignoring column names
next(reader)


# Create a list to store the customer name and country data
customer_countries = []
    

# Looping over each row in the input file
for row in reader:
    customer_full_name = row[1] + " " + row[2] 
    country = row[4]
    print(f"{customer_full_name},{country}")
    customer_countries.append((customer_full_name, country))


#Writing the extracted contents (Full_Name and Country) into a new file customer_countries.csv
output_file =  open('customer_country.csv', 'w') 
writer = csv.writer(output_file)
writer.writerow(['Full Name', 'Country'])
for customer_country in customer_countries:
    writer.writerow(customer_country)

# To close the opened output file
output_file.close()


    








