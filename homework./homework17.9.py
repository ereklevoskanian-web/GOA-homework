book_price = float(input("Enter the price of one book: "))
book_count = int(input("Enter the number of books: "))
money = float(input("Enter the amount of money you have: "))

total_cost = book_price * book_count
remaining = money - total_cost

print(f"Total cost of books: {total_cost}")
print(f"Money left after purchase: {remaining}")