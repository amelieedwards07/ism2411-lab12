# Reflection 1:
# Doing this task in Python is similar to Excel because both can organize data and calculate. Python makes it easier to automate processes and work with larger files, Excel is easier for quickly editing data without code.

# Reflection 2:
# A restaurant could use an append-mode log to record its daily sales. Append mode could be useful because it adds each new sales record without deleting the previous entries, which can allow managers to look back at past sales and track performance.

import csv
from datetime import datetime

# Exercise 4: Compute totals
total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"\nTotal Revenue: ${total_revenue:.2f}")

# Exercise 5: Filter and write cleaned CSV

original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, f"{total:.2f}"])
                cleaned_count += 1

print(f"\nOriginal rows: {original_count}")
print(f"Rows written to cleaned.csv: {cleaned_count}")

# Exercise 6: Using csv.DictReader

# csv.reader is useful for simple files when you know column positions. csv.DictReader is better when you want to access columns by name.

dict_total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"\nDictReader Total Revenue: ${dict_total_revenue:.2f}")

# Exercise 7: Sales summary by product

sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

print("\nSales Summary by Product:")

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

# Exercise 8: Append mode log

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{current_time} - Total Revenue: ${total_revenue:.2f}\n")

print("\nRun logged successfully!")
