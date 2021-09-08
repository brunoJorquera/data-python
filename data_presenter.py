open_file = open("CupcakeInvoices.csv")
# ------------------------------------------------------------------------

for loop in open_file:
    print(loop)

open_file.close()
# ------------------------------------------------------------------------

import csv
cake = open("CupcakeInvoices.csv")
csv_cake = csv.reader(cake)

for row in csv_cake:
    print(row[2])

cake.close()
# ------------------------------------------------------------------------

import csv
invoice = open("CupcakeInvoices.csv")

for row in invoice:
    row = row.rstrip("\n").split(",")
    order_price = int(row[-2])* float(row[-1])
    print("Invoice:", round(order_price,2))

invoice.close()
# ------------------------------------------------------------------------

Total = open("CupcakeInvoices.csv")

for row in Total:
    row = row.rstrip("\n").split(",")
    order_price = order_price + int(row[-2])* float(row[-1])

print("Total:", round(order_price,2))

Total.close()
# ------------------------------------------------------------------------
