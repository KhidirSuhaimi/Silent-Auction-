#Secret Auction Program

print("Welcome to the secret auction program.")
bidders ={}
end = False
while not end:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bidders[name] = bid
    next = input("Are there any other bidders?\n Type 'yes' or 'no'")
    if next == 'yes':
        end = False
    elif next == 'no':
        end = True
    print("\n" *10)
top_bid = 0
top_name = ''
for name in bidders:
    if bidders[name] > top_bid:
        top_bid = bidders[name]
        top_name = name
print(f"The winner is {top_name} with a bid of ${top_bid}.")