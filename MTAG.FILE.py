#People who worked on this was Andie, Ty, and India
import time
import random
student = ['A','B']
''.join(student)

#functions ******************************************************************************************


def weewoo():
    print(i,end='', flush = True)
    time.sleep(0.1)



money = 5
inventory = ["Phone", "Wallet",]
def vending():
    global money 
    global inventory
    item =["Pop Tart", "Doritos", "Hot Cheetos", "Sun chips", "Fruit snacks",  "Arizona half and half"]
    price = [1.50, 1.50, 1.50, 1.50, 1.50, 1.50]
    discription = ["A nice ravioli type treat", "Triangle chips", "Cheetos but hot", "Chips that are wavy", "Snacks of the fruit", "Iced tea and lemonade"]
    user_continue = "y"
    welcome = ("Welcome to Vending Co.")
    envent = ("\ninventory:", inventory, "\n")
    wall = ("money in wallet:", money ,"\n")
    ##########
    seel = ("What do you want to sell?")
    preece =  ("How much is it worth?")
    des = ("Please add a description for your item")
    sell = ("Thank you for selling your item!")
    no = ("you dont have this item.")
    buy = ("Confirm item:(y/n)")
    nomoney = ("You do not have enough money")
    done = ("Thank you for buying from Vending Co.")
    cont = ("Would you like something else? (y/n)")

    while user_continue == "y":
        for i in welcome:
            print(i,end='', flush = True)
            time.sleep(0.1)
        for i in envent:
            print(i,end='', flush = True)
            time.sleep(0.1)
        for i in wall:
            print(i,end='', flush = True)
            time.sleep(0.1)
        for i in range(len(item)):
            print(i +1, item[i], "$",price[i], discription[i])
        print((len(item)+1), "Sell an item to Vending Co.")
        user_choice = int(input("What would you like to buy?"))
        if user_choice == len(item)+1:
            for i in wall:
                print(i,end='', flush = True)
                time.sleep(0.1)
            item.append(input(""))
            for i in preece:
                print(i,end='', flush = True)
                time.sleep(0.1)
            price.append(int(input("")))
            for i in des:
                print(i,end='', flush = True)
                time.sleep(0.1)
            discription.append(input(""))
            if item[-1] in inventory:
                for i in sell:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                inventory.remove(item[-1])
                money += price[-1]
            else:
                for i in no:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                del item[-1]
                del price[-1]
                del discription[-1]
        else:
            print(item[user_choice-1])
            print(price[user_choice-1])
            print(discription[user_choice-1])
            for i in buy:
                print(i,end='', flush = True)
                time.sleep(0.1)
            buy = input("")
            if buy == "y":
                if money >= price[user_choice-1]:
                    money -= price[user_choice-1]
                    print("You have: $",money, "left")
                    inventory.append(item[user_choice-1])
                else:
                    for i in nomoney:
                        print(i,end='', flush = True)
                        time.sleep(0.1)
        print("inventory:", inventory)
        print("money in wallet: $",money)
        for i in cont:
            print(i,end='', flush = True)
            time.sleep(0.1)
        user_continue = input("")
        if user_continue == "n" or "N":
            for i in done:
                print(i,end='', flush = True)
                time.sleep(0.1)
            break
        else:
            user_continue = "y"

def clothes():
    C = ('\nHow would you like to dress today?')
    print(C),weewoo()
    Clothes = ('\n1. Comfy  2. Casual  3. Classy')    
    clothes_1 = ('It is pretty cold outside!')
    clothes_2 = ('Nice shoes!')
    clothes_3 = ('Wow! Looking good!')
    for i in Clothes:
        print(i,end='', flush = True)
        time.sleep(0.1)
    Clothes = int(input(""))
    if Clothes == 1:
        for i in clothes_1:
            print(i,end='', flush = True)
            time.sleep(0.1)
    elif Clothes == 2:
        for i in clothes_2:
            print(i,end='', flush = True)
            time.sleep(0.1)
    else:
        for i in clothes_3:
            print(i,end='', flush = True)
            time.sleep(0.1)


user_health = 3
boss_health =  3
fight = ('Time to fight for your life. Choose your weapon:')

rand_choices = ['Rock', 'Paper', 'Scissors']

tie = ("You tied...")
win = ("You won that round!")
lose = ("You lost that round, loser...")
winwin = ("You won Rock, Paper, Sissors! Congrats you have won the Life of a Student!")
loselose = ("You have lost! Restart the game!")
def rps():
    global user_health
    global boss_health
    for i in fight:
            print(i,end='', flush = True)
            time.sleep(0.1)
    while user_health != 0 or boss_health != 0:
        weapon_choice = input("(R/P/S)")
        rand_game = random.randint(0,2)
        if user_health == 0:
            for i in loselose:
                print(i,end='', flush = True)
                time.sleep(0.1)
            break
        if boss_health == 0:
            for i in winwin:
                print(i,end='', flush = True)
                time.sleep(0.1)
            break
        if weapon_choice == "R" or "r":
            if rand_game == 0:
                for i in tie:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                continue 
            elif rand_game == 1:
                for i in lose:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                user_health -= 1
                continue
            elif rand_game == 2:
                for i in win:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                boss_health -= 1
                continue
        if weapon_choice == "p" or "P":
            if rand_game == 0:
                for i in win:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                boss_health -= 1
                continue 
            elif rand_game == 1:
                for i in tie:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                continue
            elif rand_game == 2:
                for i in lose:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                user_health -= 1
                continue
        if weapon_choice == "S" or "s":
            if rand_game == 0:
                for i in lose:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                user_health -= 1
                continue 
            elif rand_game == 1:
                for i in win:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                boss_health -= 1
                continue
            elif rand_game == 2:
                for i in tie:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                continue







#this is where the things start for quest 1     *************************************************************************************************************************
start = ("Do you go to class (y/n) ")
classy = ("You go to class. You witness a fight \nDo you particapte in the fight (y/n)")
lie = ("To the principal's office. He asks if you were in the fight. \nDo you lie (y/n)")
liey = ("You get suspended. Go home")
lien = ("Take the day off. Go home")
classn = ("You get to go home. \nAre you hungry? (y/n)")
hungyy= ("You go get food.") 
hungyn = ("Go straight home. You make a sandwich")
startn= ("Hide in the bathroom. \nAre you tired? (y/n)")
tiredy = ("You've fallen asleep \nDo you want to wake up (y/n)")
wakey = ("Go to lunch")
waken = ("You slept through school. Time to go home.")
triedn = ("A teacher comes in. \nDo you make noise? (y/n) ")
noisey = ("To the principal's office.")
noisen = ("You're safe go to lunch.")

def quest1():
    global inventory
    for i in start:
        print(i,end='', flush = True)
        time.sleep(0.1)
    user_start = input("")
    if user_start == "y":
        for i in classy:
            print(i,end='', flush = True)
            time.sleep(0.1)
        user_class = input("")
        if user_class == "y":
            for i in lie:
                print(i,end='', flush = True)
                time.sleep(0.1)
            user_lie = input("")
            if user_lie == "y":
                for i in liey:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                #put code here to GO HOME
            else:
                for i in lien:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                #put code here to start the school_quest
        else:
            for i in classn:
                print(i,end='', flush = True)
                time.sleep(0.1)
            user_hungy = input("")
            if user_hungy == "y":
                for i in hungyy:
                    print(i,end='', flush = True)
                    time.sleep(0.1)
                quest2()
            else:
                for i in hungyn:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #GO HOME
    else:
        for i in startn:
            print(i,end="",flush = True)
            time.sleep(0.1)
        user_tired = input("")
        if user_tired == "y":
            for i in tiredy:
                print(i,end="",flush = True)
                time.sleep(0.1)
            user_wake = input("")
            if user_wake == "y":
                for i in wakey:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #continue onto School path
            else:
                for i in waken:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #GO HOME
        else:
            for i in triedn:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
            user_hole = input("")
            if user_hole == "y":
                for i in noisey:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                quest2()
            else:
                for i in noisen:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #GO ONTO SCHOOL PATH

#THIS IS THE VARIBLES FOR QUEST 2 #########################################################################################################
starty = ("\nYou are going to get food. Do you want fast food? (y/n) ")
fasty = ("You are thinking about fast food.\nDo you want chicken nuggets? (y/n)")
placew = ("Choose a place.\nWendys or McDonalds (w/m)")
micnugs = ("You go to McDonalds and have aquired the nuggies.")
wend = ("You go to Wendy's and have aquired the nuggies.")
nonug = ("Damn no nuggies. Okay...\nDo you want White Castle. (y/n)")
whitey = ("You go to White Castle. (gross)")
whiten = ("You go make a sandwich at home.")
fastn = ("Don't like fast food... me too... \nDo you want a bagel (y/n)")
bagley =("Bagels are good. \nPanera? (y/n) ")
panera = ("You go get Panera.")
timhortins = ("You go to Tim Hortons")
baglen = ("No Bagels? Boo Hoo. \nEgg Sandwich? (y/n)")
eggy = ("Go to McDonalds and get an Egg Sandwich.")
eggn = ("Go home and make a sandwich.")

def quest2():
    global user_health
    global user_money
    global inventory
    for i in starty:
        print(i,end="",flush = True)
        time.sleep(0.1)
    user_start = input("")
    if user_start == "y":
        for i in fasty:
            print(i,end="",flush = True)
            time.sleep(0.1)
        user_gum = input('')
        if user_gum == "y":
            for i in placew:
                print(i,end="",flush = True)
                time.sleep(0.1)
            user_gum_eat = input("")
            if user_gum_eat == "m":
                inventory.append("nuggies")
                for i in micnugs: 
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                print(go_home)
            else:
                for i in wend:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                inventory.append("nuggies")
                print(go_home) 
        else:
            for i in nonug:
                print(i,end="",flush = True)
                time.sleep(0.1)
            user_hole = input("")
            if user_hole == "y":
                for i in whitey:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                inventory.append("White Castle Fries")
                print(go_home)
            else:
                for i in whiten:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                inventory.append("Sandwich")
                print(go_home)
    else:
        for i in fastn:
            print(i,end="",flush = True)
            time.sleep(0.1)
        user_shiny = input("")
        if user_shiny == "y":
            for i in bagley:
                print(i,end="",flush = True)
                time.sleep(0.1)
            user_shiny_eat = input("")
            if user_shiny_eat == "y":
                inventory.append("Panera bagel")
                for i in panera:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                print(go_home)
            else:
                for i in timhortins:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                inventory.appened("Tim Hortons Bagel")
                print(go_home)
        else:
            for i in baglen:
                print(i,end="",flush = True)
                time.sleep(0.1)
            user_hole = input("")
            if user_hole == "y":
                for i in eggy:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                inventory.append("Mcdonalds Egg Sandwich")
                print(go_home)
            else:
                for i in eggn:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                inventory.append("Sandwich")
                print(go_home)

#QUEST 3 VARIABLES ############################################################################################################################

princstart = ('Do you argue with the principal? (y/n)')
pricy = ("The principal slaps your hand. \nDo you fight back? (y/n)")
fighty = ("Uh Oh... \nDo you want to start the boss battle? (y/n)")
boosy = ("Get ready...")
boosn = ("You get suspended. Go home.")
fighn = ("Oh come on fight back! \nYou think of fighting. Do you want to fight back?  (y/n)")
fight2 = ("Uh Oh you started a boss fight get ready....") 
sus = ("You've been suspended. Go home.")
arguen = ("He rewards you with going home. \nDo you want to go home? (y/n)")
hoom = ("You drive home. You walk in the door. \nIt's been a long day. Do you want to go to bed? (y/n)")
game = ("Game over.")
foodsie = ("Do you want to go get food? (y/n)")
momfight = ("You see your mother.")
princble = ("The principal slaps you in the hand. \nDo you fight back? (y/n)")
boosprin = ("Uh oh... you started the boss battle ... get ready.")
cow = ("Cower in fear... You are soon released. Go home")

def quest3():
    global user_health
    global user_money
    global inventory
    for i in princstart:
        print(i,end="",flush = True)
        time.sleep(0.1)
    user_start = input("")
    if user_start == "y":
        for i in pricy:
            print(i,end="",flush = True)
            time.sleep(0.1)
        user_class = input("")
        if user_class == "y":
            for i in fighty:
                print(i,end="",flush = True)
                time.sleep(0.1)  
            user_gum_eat = input("")
            if user_gum_eat == "y":
                for i in boosy:
                    print(i,end="",flush = True)
                    time.sleep(0.1) 
                #FUCKING START BOSS BAATTLE
            else:
                for i in boosn:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #GO HOME CODE
        else:
            for i in fighn:
                print(i,end="",flush = True)
                time.sleep(0.1)
            user_hole = input("")
            if user_hole == "y":
                for i in fight2:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #STARTS BOSS BATTLE AHHHHHHHHHHHHHHHHHHHHHHH
            else:
                for i in sus:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #put code here to go home
    else:
        for i in arguen:
            print(i,end="",flush = True)
            time.sleep(0.1)
        user_shiny = input("")
        if user_shiny == "y":
            for i in hoom:
                print(i,end="",flush = True)
                time.sleep(0.1)
            user_shiny_eat = input("")
            if user_shiny_eat == "y":
                for i in game:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #GAME OVER
            else:
                for i in foodsie:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                user_food = input("")
                if user_food == "y":
                    quest2()
                else:
                    for i in momfight:
                        print(i,end="",flush = True)
                        time.sleep(0.1)
                    #start mother boss battle
        else:
            for i in princable:
                print(i,end="",flush = True)
                time.sleep(0.1)
            user_hole = input("")
            if user_hole == "y":
                for i in boosprin:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #BOSS BATTLE STARTS
            else:
                for i in cow:
                    print(i,end="",flush = True)
                    time.sleep(0.1)
                #CONTINUE ONTO HOME


#variables that are being tracked ******************************************************************************************************


Begin = ('Welcome to The Life of a Student! Please choose your character: ')
for i in Begin:
    weewoo()


water=('\n*water sounds...*')
bathroom=("\nTo the bathroom!")
snooze= ("zzzZzzzZzzZ\nzzZzzZZzz\n...Waking up...")
Characters = input('A or B')
wake = ("zzZzzZ \n...Waking up...")
Choice_1 = ('\n1. Snooze or 2. Get out of bed ') 

if Characters == 'A' or 'a':
    for i in wake:
        weewoo()

for i in Choice_1:
    weewoo()
Choice_1 = int(input('')) 

if Choice_1 == 1:
    for i in snooze:
        weewoo()

for i in bathroom:
    weewoo()
for i in water:
    weewoo()      
    
clothes()


School = ('\nWhat school do you go to?')
Options = ('\n1. John Glenn High School or 2. Allen Park High School ')
Class = ("")

for i in School:
   weewoo()
for i in Options:
    weewoo()
School = int(input(""))

Transport = ('Choose mode of transportation: 1. Bus 2. Car')
 
for i in Transport:
    weewoo()

TPort = int(input(""))
Bus= ("Vrooomm.. \n*bus stops suddenly*\n*slams head into seat in front*") #doesn't hit head
Driving = ("\nVrooooooom...")
Arrive= ('\nYou have arrived!')
Quest = ('\nWhere would you like to go?')
woo = ('\n1. Front Door, 2. Back Door')

if TPort == 1:
    for i in Bus:
        weewoo()

for i in Driving:
    weewoo()

for i in Arrive:
    weewoo()

rand_money = random.randint(1,10)
pickup = ("\nYou find money on the ground! \nDo you want to pick up the money? (y/n)")
findmone = ("You have found $" + str(rand_money))
mom = ("\nYou now have $", int(rand_money) + int(money))
che = ("You did not pick up the money",)
for i in pickup:
    weewoo()
ground_money = input("")
if ground_money == "y":
    money = money + rand_money
    for i in findmone:
        weewoo()
    for i in mom:
        weewoo()
else:
    for i in che:
        weewoo()
    for i in mom:
        weewoo()
    

for i in Quest:
    weewoo()

for i in woo:
    weewoo()
woo = int(input(''))

front = ('\n*sighs*... Time for another day.')
back = ('\nNot again...')
go_home = ('\nYou\'ve encounted your final match.')
bye = 1#put in rock paper scissors mod 
goodbye = ('Congrats! You have finished the game.')
mmm = ('You have lost.')



while woo == 2:
    for i in back:
        weewoo()
    


if woo == 1:
    for i in front:
        weewoo()
    front = input('-press enter to continue-')

for i in quest1():
    weewoo()

for i in go_home:
    weewoo()
    go_home = input('-press enter to continue-')




#CHARACTER B *************************************************************************************

wake = ("zzZzzZ \n...Waking up...")

if Characters == 'B' or 'b':
    for i in wake:
        weewoo()

water=('\n*water sounds...*')
bathroom=("\nTo the bathroom!")
snooze= ("zzzZzzzZzzZ\nzzZzzZZzz\n...Waking up...")


for i in Choice_1:
    weewoo()
Choice_1 = int(input(''))

if Choice_1 == 1:
    for i in snooze:
        weewoo()
    
for i in bathroom:
   weewoo()
for i in water:
    weewoo()

clothes()

School = ('\nWhat school do you go to?')
Options = ('\n1. John Glenn High School or 2. Allen Park High School')
Class = ("")

for i in School:
   weewoo()
for i in Options:
    weewoo()
School = int(input(""))

Transport = ('Choose mode of transportation: 1. Bus 2. Car')
 
for i in Transport:
    weewoo()
TPort = int(input(""))
Bus= ("Vrooomm.. *bus stops suddenly*\n*slams head into seat in front")
Driving = ("\nVrooooooom...")
Arrive= ('\nYou have arrived!')
Quest = ('\nWhere would you like to go?')
woo = ('\n1. Front Door, 2. Back Door')

for i in Driving:
    weewoo()

for i in Arrive:
    weewoo()

for i in Quest:
    weewoo()

rand_money = random.randint(1,10)
pickup = ("You find money on the ground! \n Do you want to pick up the money (y/n)")
findmone = ("You have found $" + str(rand_money))
mom = ("You now have $" + str(money))
che = ("You did not pick up the money")
for i in pickup:
    weewoo()
ground_money = input("")
if ground_money == "y":
    money = money + rand_money
    for i in findmone:
        weewoo()
    for i in mom:
        weewoo()
else:
    for i in che:
        weewoo()
    for i in mom:
        weewoo()

for i in woo:
    weewoo()
woo = int(input(''))

front = ('\n*sighs*... Time for another day.')
back = ('\nNot again...')

if woo == 1:
    for i in front:
        weewoo()
    front = input('-press enter to continue-')

for i in back:
    weewoo()