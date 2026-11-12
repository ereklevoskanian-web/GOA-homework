time = input ("What time do you want? ")
teem = input ("Which team's game do you want to watch?")
football_match = input (" How many tickets do you want? ")
tickets_price = 30
total = tickets_price * int(football_match)
print (" The total cost for " + football_match + " tickets to the " + teem + " game at " + time + " is $" + str(total))