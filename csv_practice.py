
import csv

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
