#1 

name = input("what is your name? ")
old  = input ("what is your old? ")
print (type(name))
print (type(old))


#2 

print ("hello")
film = input ("Which movie do you want? ")
time = input ("What time do you want? ")
tickets = input ("How many ticket do you want?")
ticket_price = 15
total =  int(ticket_price * tickets)
print ("your want " + film, "You want to, at this moment " + time, "You want this many tickets" + tickets, "total" + int(total), "$" )