#Simple phone book using hash tables

phone_book = dict();

phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

print(phone_book["jenny"])

#Voting booth using hash tables

voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")