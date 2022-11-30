import csv
default = {}
1
# reading csv file
with open("coffee.csv", 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    header = next(csvreader)
    for row in csvreader:
        default[row[0]] = int(row[1])



coffee_cup = r"""

  /~~~~~~~~~~~~~~~~~~~/|
        /              /######/ / |
      /              /______/ /  |
      ========================= /||
      |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||       
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~buybuy
    

                                            (  )   (   )  )
                                              ) (   )  (  (
                                              ( )  (    ) )
                                              _____________
                                             <_____________> ___
                                             |             |/ _ \
                                             |               | | |
                                             |               |_| |
                                          ___|             |\___/
                                        /    \___________/    \
                                        \_____________________/

"""


money = r"""
    ||====================================================================||
    ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
    ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
    ||\\$//        ~         '------========--------'                \\$//||
    ||<< /        /$\              // ____ \\                         \ >>||
    ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
    ||<<|        \\ //           || <||  >\  ||                        |>>||
    ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF indiaaanna|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
"""



thanks = r"""
═✿✿✿═════✿✿═════✿✿═════✿✿✿═
════════════ ('\../') ═════════════
════════════ (◕.◕) ═════════════
════════════ (,,)(,,) ═════════════
.▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█
─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█
"""


# print(default["water"])


water_fill = 0
milk_fill = 0
beans_fill = 0
cups_fill = 0
filled_water = default["water"] + water_fill
filled_milk = default["milk"] + milk_fill
filled_beans = default["beans"] + beans_fill
filled_cups = default["cups"] + cups_fill

#def_ == water in coffee machine
#actual_ == water coffee requires

def buy():
    # global def_money
    coffeetype = input("What do you want to buy? 1 - espresso($4), 2 - latte(7$), 3 - cappuccino($6), back - to main menu:")
    print("")
    global actual_water
    global actual_beans
    global actual_money
    global actual_milk
    # if coffeetype == "back":
    #     mainmenu()
    if coffeetype == "back":
        mainmenu()
    else:
        if coffeetype == "1":
            actual_water = 250
            actual_milk = 0
            actual_beans = 16
            actual_money = 4
        elif coffeetype == "2":
            actual_water = 350
            actual_milk = 75
            actual_beans = 20
            actual_money = 7
        elif coffeetype == "3":
            actual_water = 200
            actual_milk = 100
            actual_beans = 12
            actual_money = 6
        # elif coffeetype == "back":
        #     Mainmenu()

        global filled_water
        global filled_beans
        global filled_milk
        global filled_cups
        if filled_water <= actual_water:
            print("Sorry, not enough water!")
        elif filled_milk <= actual_milk:
            print("Sorry, not enough milk!")
        elif filled_beans <= actual_beans:
            print("Sorry, not enough coffee beans!")
        elif filled_cups == 0:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            print(coffee_cup)
            filled_cups = filled_cups - 1
            filled_water = filled_water - actual_water
            filled_milk = filled_milk - actual_milk
            filled_beans = filled_beans - actual_beans
            default["money"] = default["money"] + actual_money
        #print(filled_water)
        print("")

def take():
    # global def_money
    print("${} withdrawn".format(default["money"]))
    default["money"] = 0
    print("")
    print(money)


def fill():
    global filled_water
    global filled_beans
    global filled_milk
    global filled_cups
    global water_fill
    global milk_fill
    global beans_fill
    global cups_fill
    water_fill = int(input("Write how many ml of water do you want to add:"))
    milk_fill = int(input("Write how many ml of milk do you want to add:"))
    beans_fill = int(input("Write how many grams of coffee beans do you want to add:"))
    cups_fill = int(input("Write how many disposable cups of coffee do you want to add:"))
    filled_water = filled_water + water_fill
    filled_milk = filled_milk + milk_fill
    filled_beans = filled_beans + beans_fill
    filled_cups = filled_cups + cups_fill
    #print(filled_water)





def remaining():
    print("The coffee machine has:")
    print(filled_water, "of water")
    print(filled_milk, "of milk")
    print(filled_beans, "of coffee beans")
    print(filled_cups, "of disposable cups")
    print("${} of money".format(default["money"]))


def mainmenu():
    while True:
        action = input("Write action (buy -1 , refill - 2, withdraw - 3, remaining - 4, exit):")
        if action == "1":
            buy()
        elif action == "2":
            fill()
        elif action == "3":
            take()
        elif action == "4":
            remaining()
        elif action == "exit":
            print(thanks)
            break
     


mainmenu()

