#Importing csv module
import csv

# Open the input file in read mode
input_file = open('sales.csv', 'r') 
reader = csv.reader(input_file)
    
# Ignore the columns
next(reader)
    
# Create an empty dictionary to store the total sales for each customer
sales_totals = {}


#Loop over each row in the input file
for row in reader:
# Extract the customer ID and sale amount from the row
    CustomerID = row[0]
    SubTotal = row[3]
    TaxAmt = row[4]
    Freight = row[5]
# Converting strings to float   
    a = float(SubTotal)
    b = float(TaxAmt)
    c = float(Freight)
    sale_amount = a + b + c 
    
# Fill the total sales for the customer in the dictionary
    if CustomerID in sales_totals:
        sales_totals[CustomerID] += sale_amount
    else:
        sales_totals[CustomerID] = sale_amount
       

# Open the output file for writing
output_file = open('salesreport.csv', 'w')


writer = csv.writer(output_file)

# Write the column names
writer.writerow(['Customer', 'Total'])

# Write each customerID and total_sales to the output file
for customer_id, total_sales in sales_totals.items():
    writer.writerow([customer_id, total_sales])

# Closing the file
output_file.close()