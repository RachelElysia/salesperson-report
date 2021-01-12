"""Generate sales report showing total melons each salesperson sold."""

def sales_report(file):
    """Input a file of sales and returns a print out of melon sales by salesperson."""

    sales_summary = open(file)

    sales = {}

    # Strip lines of whitespace and split entries by name, revenue, and melons.
    for entry in sales_summary:
        entry = entry.rstrip().split('|')

        # Create new key value pair if not in dictionary,
        # otherwise add to salesperson revenue (int).
        if entry[0] not in sales.keys():
            sales[entry[0]] = int(entry[2])
        else:
            sales[entry[0]] += int(entry[2])

    # Print statment by sales person (key str) including melons_sold (value int),
    for salesperson, melons_sold in sales.items():
        print(f'{salesperson} sold {melons_sold} melons.')

sales_report('sales-report.txt')