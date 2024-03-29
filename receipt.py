#I have added code that will look at the day of the week and add a subtotal discount if its Tuesday or Wednesday

import csv
from datetime import datetime
current_date_and_time = datetime.now()

# Use an f-string to print the current
# day of the week and the current time.

product_name = 1
requested_quantity = 1
product_number = 0
product_price = 2


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary ={}

    with open(filename, mode="rt") as test_file:
        reader = csv.reader(test_file)
        next(reader)
        for row_list in reader:
            if len(row_list) !=0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary


def main():
    try:
        total_quantity = 0
        subtotal = 0
        products_dict = read_dictionary("products.csv", 0)
        print(f"All Products:")
        print(products_dict)
        with open("request.csv", mode="rt") as test_file:
            reader = csv.reader(test_file)
            next(reader)
            print()
            print(f"Fast and Speedy Purchase Receipt:")
            print()
            for row_list in reader:
                quantity = int(row_list[requested_quantity])
           
                number = row_list[product_number]

                product_id = products_dict[number]
            
                name = product_id[product_name]
                price = float(product_id[product_price])

                print(f"{name} : {quantity} @ {price}")

                total_quantity += quantity
                subtotal += price
    except KeyError as Error:
        print(f"Error: unknown product ID in the request.csv file'{Error}")
    except FileNotFoundError as not_found_err:
        print(not_found_err)
        
    if (f'{current_date_and_time:%A}') == "Tuesday":
        subtotal = subtotal * .90

    if (f'{current_date_and_time:%A}') == "Wednesday":
        subtotal = subtotal * .90

    sales_tax = subtotal * .06

    total = subtotal + sales_tax

    print(f'{current_date_and_time:%A}')
            
    print()
    print(f'Number of Items: {total_quantity}')
    print(f'Subtotal: ${subtotal:,.2f}')
    print(f'Sales Tax: ${sales_tax:,.2f}')
    print(f'Total: ${total:,.2f}')
    print()
    print(f"Thank you for shopping at the Fast and Speedy")
    print(f"{current_date_and_time:%A %I:%M %p}")
  

if __name__ == "__main__":
    main()