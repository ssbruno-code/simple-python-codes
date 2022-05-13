auction = []
turn = "true"

def addNewBid(name, value):
    bid = {
        "name": name,
        "value": value,
    }
    auction.append(bid)
    
def verifyWinner():
    bidName = ""    
    bidValue = 0
    for bid in auction:    
        if bidValue <= bid["value"]:
            bidName = bid["name"]
            bidValue = bid["value"]            
        
    print(f"The Winner is {bidName} with the bid {bidValue}\n")
    print(auction)

print("""
                                     .-===-.
                                      \   /
                                      |   |
                                    __|:::|__
       .-===-.                 _.--'  |:::|  `-._
        \   /           __    /      (:::::)     
        |:::|          |  |   \       `---'      /
      __|:::|__        |..|    ``--...____...--''
 _.--'  |:::|  `-._   /_/\_\     ___..-(O/
/      (:::::)     \  |  __...--' __..-''
\       `---'      /_.--(o)_...--'
 ``--...____...--''__..--'_|
        \O)___..--'   \ \/ /
         .-------------|''|-------------.
        /              |__|              
       /__________________________________|
       '----------------------------------'
      Hello! Welcome to the Secret Auction, please put your bids for the item:      
      there is no Draw, the last one who bids gets the item in case of a Draw""")

while turn != "false":
    getName = input("What is your name?\n")
    getBid = int(input("What is your bid?\n"))
    addNewBid(getName, getBid)
    nextTurn = input("Anyone else wants to make a bid? Type 'yes' or 'no'\n")
    if nextTurn == "no":
        turn = "false"

verifyWinner()