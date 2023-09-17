casino_blacklist = ['John Doe', 'Jason Statham', 'Victor Krauff', 'Vasil Petrov']
poker_blacklist = ['Jane Doe', 'Will Smith', 'Vasil Petrov', 'Victor Krauff']
alcohol_blacklist = ['Mark Twen', 'Alan Poe', 'Vasil Petrov', 'Victor Krauff']
name = input(str("Find name: "))
casino = name in casino_blacklist
poker = name in poker_blacklist
alco = name in alcohol_blacklist
if casino and poker and alco:
    print("In all blacklists")
else:
    print("Not in all blacklists")
