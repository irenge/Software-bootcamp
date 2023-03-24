abbrev = { 
         "ADSL": "Asymmetric Digital Subscriber Line",
         "IP": "Internet Protocol",
         "TCP": "Transmission Control Protocol",
         "UDP": "User Datagram Protocol"
         
         }


x = input("Enter an abbreviation: ").upper()

if x in abbrev:
    print(f"{x}: {abbrev[x]}")
else:
    print("Not found")
