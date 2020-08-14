def chess_and_crackers(chess_count, boxes_of_crackers):
    print(f"You have {chess_count} chesses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket .\n")


print("We can just give the function numbers directly:")
chess_and_crackers(20,30)

print("OR,we can use variables from our script:")
amount_of_chess = 10
amount_of_crackers = 50

chess_and_crackers(amount_of_chess, amount_of_crackers)

print("We can even do math inside too:")    
chess_and_crackers(10+20,5+6)

print("And we can combine the two, variables and math:")
chess_and_crackers(amount_of_chess + 100,amount_of_crackers + 1000)