import time
import random
import threading
import ast


def errorfix(error, var):
    match error:
        case 1:
            if var is not "":
                var = int(var)
            else:
                menu(1)


equicheck = True
equi_lock = threading.Lock()

rng_range = 1000000

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0

old_boats = 0
normal_boats = 0
big_boats = 0
yachts = 0
ships = 0
whaling_ships = 0

ol = 0.5
no = 0.5
bi = 0.5
ya = 0.5
sh = 0.5
wh = 0.5

old = 0
nor = 0
big = 0
yac = 0
shi = 0
wha = 0

megaharpoon = False
harpoon = False
dragonbait = False
goodrod = False

goodrodused = False
dragonbaitused = False
harpoonused = False
megaharpoonused = False

money = 0
diffquantity = [1]
z = 1
quantity = 1
multiplier = 1

mortezas = 0
cods = 0
mr_crabs = 0
sharks = 0
collossal_squid = 0
squids = 0
blue_whales = 0
sea_dragons = 0
megalodons = 0
shrimps = 0
old_boots = 0
salmons = 0

fish = 0

mor = 1
cod = 800000
mrc = 3000
sha = 1500
col = 500
squ = 70000
blu = 1000
sea = 10
meg = 100
shr = 300000
boot = 20000
sal = 650000


def save(x):
    global sal, boot, shr, meg, sea, blu, squ, col, sha, mrc, cod, mor, salmons, old_boots, shrimps, megalodons, sea_dragons, blue_whales, squids, collossal_squid, sharks, mr_crabs, cods, mortezas, multiplier, quantity, diffquantity, money, megaharpoonused, harpoonused, dragonbaitused, goodrodused, goodrod, dragonbait, harpoon, megaharpoon, wha, shi, yac, big, nor, old, wh, sh, ya, bi, no, ol, whaling_ships, ships, yachts, big_boats, normal_boats, old_boats, k, j, i, h, g, f, e, d, c, b, a, rng_range, equicheck
    match x:
        case "1":
            with open("game_memory/user1_morteza_fishing.txt", "w") as user_one:
                user_one.write(
                    f"{sal}\n{boot}\n{shr}\n{meg}\n{sea}\n{blu}\n{squ}\n{col}\n{sha}\n{mrc}\n{cod}\n{mor}\n{salmons}\n{old_boots}\n{shrimps}\n{megalodons}\n{sea_dragons}\n{blue_whales}\n{squids}\n{collossal_squid}\n{sharks}\n{mr_crabs}\n{cods}\n{mortezas}\n{multiplier}\n{quantity}\n{diffquantity}\n{money}\n{megaharpoonused}\n{harpoonused}\n{dragonbaitused}\n{goodrodused}\n{goodrod}\n{dragonbait}\n{harpoon}\n{megaharpoon}\n{wha}\n{shi}\n{yac}\n{big}\n{nor}\n{old}\n{wh}\n{sh}\n{ya}\n{bi}\n{no}\n{ol}\n{whaling_ships}\n{ships}\n{yachts}\n{big_boats}\n{normal_boats}\n{old_boats}\n{k}\n{j}\n{i}\n{h}\n{g}\n{f}\n{e}\n{d}\n{c}\n{b}\n{a}\n{rng_range}\n{equicheck}"
                )
        case "2":
            with open("game_memory/user2_morteza_fishing.txt", "w") as user_one:
                user_one.write(
                    f"{sal}\n{boot}\n{shr}\n{meg}\n{sea}\n{blu}\n{squ}\n{col}\n{sha}\n{mrc}\n{cod}\n{mor}\n{salmons}\n{old_boots}\n{shrimps}\n{megalodons}\n{sea_dragons}\n{blue_whales}\n{squids}\n{collossal_squid}\n{sharks}\n{mr_crabs}\n{cods}\n{mortezas}\n{multiplier}\n{quantity}\n{diffquantity}\n{money}\n{megaharpoonused}\n{harpoonused}\n{dragonbaitused}\n{goodrodused}\n{goodrod}\n{dragonbait}\n{harpoon}\n{megaharpoon}\n{wha}\n{shi}\n{yac}\n{big}\n{nor}\n{old}\n{wh}\n{sh}\n{ya}\n{bi}\n{no}\n{ol}\n{whaling_ships}\n{ships}\n{yachts}\n{big_boats}\n{normal_boats}\n{old_boats}\n{k}\n{j}\n{i}\n{h}\n{g}\n{f}\n{e}\n{d}\n{c}\n{b}\n{a}\n{rng_range}\n{equicheck}"
                )
        case "3":
            with open("game_memory/user3_morteza_fishing.txt", "w") as user_one:
                user_one.write(
                    f"{sal}\n{boot}\n{shr}\n{meg}\n{sea}\n{blu}\n{squ}\n{col}\n{sha}\n{mrc}\n{cod}\n{mor}\n{salmons}\n{old_boots}\n{shrimps}\n{megalodons}\n{sea_dragons}\n{blue_whales}\n{squids}\n{collossal_squid}\n{sharks}\n{mr_crabs}\n{cods}\n{mortezas}\n{multiplier}\n{quantity}\n{diffquantity}\n{money}\n{megaharpoonused}\n{harpoonused}\n{dragonbaitused}\n{goodrodused}\n{goodrod}\n{dragonbait}\n{harpoon}\n{megaharpoon}\n{wha}\n{shi}\n{yac}\n{big}\n{nor}\n{old}\n{wh}\n{sh}\n{ya}\n{bi}\n{no}\n{ol}\n{whaling_ships}\n{ships}\n{yachts}\n{big_boats}\n{normal_boats}\n{old_boats}\n{k}\n{j}\n{i}\n{h}\n{g}\n{f}\n{e}\n{d}\n{c}\n{b}\n{a}\n{rng_range}\n{equicheck}"
                )


def load(x):
    global sal, boot, shr, meg, sea, blu, squ, col, sha, mrc, cod, mor, salmons, old_boots, shrimps, megalodons, sea_dragons, blue_whales, squids, collossal_squid, sharks, mr_crabs, cods, mortezas, multiplier, quantity, diffquantity, money, megaharpoonused, harpoonused, dragonbaitused, goodrodused, goodrod, dragonbait, harpoon, megaharpoon, wha, shi, yac, big, nor, old, wh, sh, ya, bi, no, ol, whaling_ships, ships, yachts, big_boats, normal_boats, old_boats, k, j, i, h, g, f, e, d, c, b, a, rng_range, equicheck
    match x:
        case "1":
            with open("game_memory.zip/user1_morteza_fishing.txt", "r") as user_one:
                line = user_one.read().splitlines()

                sal = float(line[0])
                boot = float(line[1])
                shr = float(line[2])
                meg = float(line[3])
                sea = float(line[4])
                blu = float(line[5])
                squ = float(line[6])
                col = float(line[7])
                sha = float(line[8])
                mrc = float(line[9])
                cod = float(line[10])
                mor = float(line[11])
                salmons = int(line[12])
                old_boots = int(line[13])
                shrimps = int(line[14])
                megalodons = int(line[15])
                sea_dragons = int(line[16])
                blue_whales = int(line[17])
                squids = int(line[18])
                collossal_squid = int(line[19])
                sharks = int(line[20])
                mr_crabs = int(line[21])
                cods = int(line[22])
                mortezas = int(line[23])
                multiplier = float(line[24])
                quantity = int(line[25])
                diffquantity = ast.literal_eval(line[26])
                money = float(line[27])
                megaharpoonused = line[28].strip() == "True"
                harpoonused = line[29].strip() == "True"
                dragonbaitused = line[30].strip() == "True"
                goodrodused = line[31].strip() == "True"
                goodrod = line[32].strip() == "True"
                dragonbait = line[33].strip() == "True"
                harpoon = line[34].strip() == "True"
                megaharpoon = line[35].strip() == "True"
                wha = float(line[36])
                shi = float(line[37])
                yac = float(line[38])
                big = float(line[39])
                nor = float(line[40])
                old = float(line[41])
                wh = float(line[42])
                sh = float(line[43])
                ya = float(line[44])
                bi = float(line[45])
                no = float(line[46])
                ol = float(line[47])
                whaling_ships = float(line[48])
                ships = float(line[49])
                yachts = float(line[50])
                big_boats = float(line[51])
                normal_boats = float(line[52])
                old_boats = float(line[53])
                k = float(line[54])
                j = float(line[55])
                i = float(line[56])
                h = float(line[57])
                g = float(line[58])
                f = float(line[59])
                e = float(line[60])
                d = float(line[61])
                c = float(line[62])
                b = float(line[63])
                a = float(line[64])
                rng_range = int(line[65])
                equicheck = line[66].strip() == "True"

        case "2":
            with open("game_memory.zip/user2_morteza_fishing.txt", "r") as user_two:
                line = user_two.read().splitlines()

                sal = float(line[0])
                boot = float(line[1])
                shr = float(line[2])
                meg = float(line[3])
                sea = float(line[4])
                blu = float(line[5])
                squ = float(line[6])
                col = float(line[7])
                sha = float(line[8])
                mrc = float(line[9])
                cod = float(line[10])
                mor = float(line[11])
                salmons = int(line[12])
                old_boots = int(line[13])
                shrimps = int(line[14])
                megalodons = int(line[15])
                sea_dragons = int(line[16])
                blue_whales = int(line[17])
                squids = int(line[18])
                collossal_squid = int(line[19])
                sharks = int(line[20])
                mr_crabs = int(line[21])
                cods = int(line[22])
                mortezas = int(line[23])
                multiplier = float(line[24])
                quantity = int(line[25])
                diffquantity = ast.literal_eval(line[26])
                money = float(line[27])
                megaharpoonused = line[28].strip() == "True"
                harpoonused = line[29].strip() == "True"
                dragonbaitused = line[30].strip() == "True"
                goodrodused = line[31].strip() == "True"
                goodrod = line[32].strip() == "True"
                dragonbait = line[33].strip() == "True"
                harpoon = line[34].strip() == "True"
                megaharpoon = line[35].strip() == "True"
                wha = float(line[36])
                shi = float(line[37])
                yac = float(line[38])
                big = float(line[39])
                nor = float(line[40])
                old = float(line[41])
                wh = float(line[42])
                sh = float(line[43])
                ya = float(line[44])
                bi = float(line[45])
                no = float(line[46])
                ol = float(line[47])
                whaling_ships = float(line[48])
                ships = float(line[49])
                yachts = float(line[50])
                big_boats = float(line[51])
                normal_boats = float(line[52])
                old_boats = float(line[53])
                k = float(line[54])
                j = float(line[55])
                i = float(line[56])
                h = float(line[57])
                g = float(line[58])
                f = float(line[59])
                e = float(line[60])
                d = float(line[61])
                c = float(line[62])
                b = float(line[63])
                a = float(line[64])
                rng_range = int(line[65])
                equicheck = line[66].strip() == "True"

        case "3":
            with open("game_memory.zip/user3_morteza_fishing.txt", "r") as user_three:
                line = user_three.read().splitlines()

                sal = float(line[0])
                boot = float(line[1])
                shr = float(line[2])
                meg = float(line[3])
                sea = float(line[4])
                blu = float(line[5])
                squ = float(line[6])
                col = float(line[7])
                sha = float(line[8])
                mrc = float(line[9])
                cod = float(line[10])
                mor = float(line[11])
                salmons = int(line[12])
                old_boots = int(line[13])
                shrimps = int(line[14])
                megalodons = int(line[15])
                sea_dragons = int(line[16])
                blue_whales = int(line[17])
                squids = int(line[18])
                collossal_squid = int(line[19])
                sharks = int(line[20])
                mr_crabs = int(line[21])
                cods = int(line[22])
                mortezas = float(line[23])
                multiplier = int(line[24])
                quantity = int(line[25])
                diffquantity = ast.literal_eval(line[26])
                money = float(line[27])
                megaharpoonused = line[28].strip() == "True"
                harpoonused = line[29].strip() == "True"
                dragonbaitused = line[30].strip() == "True"
                goodrodused = line[31].strip() == "True"
                goodrod = line[32].strip() == "True"
                dragonbait = line[33].strip() == "True"
                harpoon = line[34].strip() == "True"
                megaharpoon = line[35].strip() == "True"
                wha = float(line[36])
                shi = float(line[37])
                yac = float(line[38])
                big = float(line[39])
                nor = float(line[40])
                old = float(line[41])
                wh = float(line[42])
                sh = float(line[43])
                ya = float(line[44])
                bi = float(line[45])
                no = float(line[46])
                ol = float(line[47])
                whaling_ships = float(line[48])
                ships = float(line[49])
                yachts = float(line[50])
                big_boats = float(line[51])
                normal_boats = float(line[52])
                old_boats = float(line[53])
                k = float(line[54])
                j = float(line[55])
                i = float(line[56])
                h = float(line[57])
                g = float(line[58])
                f = float(line[59])
                e = float(line[60])
                d = float(line[61])
                c = float(line[62])
                b = float(line[63])
                a = float(line[64])
                rng_range = int(line[65])
                equicheck = line[66].strip() == "True"


def equipment_check():
    global equicheck, goodrod, dragonbait, harpoon, megaharpoon, rng_range, mor, sea, goodrodused, dragonbaitused, harpoonused, megaharpoonused, old_boats, normal_boats, big_boats, yachts, ships, whaling_ships, ol, no, bi, ya, sh, wh, quantity, diffquantity, multiplier, blu, sha, meg, mrc, col
    with equi_lock:
        while equicheck == True:

            if goodrod == True and goodrodused == False:
                rng_range -= 200000
                multiplier += 1
                goodrodused = True
            if goodrod == False and goodrodused == True:
                rng_range += 200000
                multiplier -= 0.5
                goodrodused = False

            if dragonbait == True and dragonbaitused == False:
                mor += 10
                sea += 100
                dragonbaitused = True
            if dragonbait == False and dragonbaitused == True:
                mor -= 10
                sea -= 100
                dragonbaitused = False

            if harpoon == True and harpoonused == False:
                blu += 9000
                sha += 13500
                mrc += 14000
                harpoonused = True
            if harpoon == False and harpoonused == True:
                blu -= 9000
                sha -= 13500
                mrc -= 14000
                harpoonused = False

            if megaharpoon == True and megaharpoonused == False:
                meg += 2000
                col += 5000
                blu += 9000
                sha += 13500
                mrc += 14000
                megaharpoonused = True
            if megaharpoon == False and megaharpoonused == True:
                meg -= 2000
                col -= 5000
                blu -= 9000
                sha -= 13500
                mrc -= 14000
                megaharpoonused = False

            if old_boats >= ol:
                if quantity < 24:
                    quantity += 1
                ol += 1

            if normal_boats >= no:
                diffquantity += [1]
                no += 1

            if big_boats >= bi:
                rng_range -= 10000
                bi += 1

            if yachts >= ya:
                multiplier += 1
                ya += 1

            if ships >= sh:
                if rng_range >= 100000:
                    rng_range -= 50000
                diffquantity += [1] * 5
                mor += 5
                sea += 6
                sh += 1

            if whaling_ships >= wh:
                if blu <= 10000 and sha <= 15000:
                    mor += 7
                    sea += 8
                    meg += 100
                    blu += 1000
                    sha += 1500
                diffquantity += [1] * 50
                multiplier += 2
                wh += 1


def buy(type, price: int, version: int):
    global money
    if version == 2:
        if money >= price:
            money -= price
            return 1
    elif money >= price and type != True:
        money -= price
        return 1
    else:
        return 0


def sell(type, price: int, type2):
    global money, mortezas, sea_dragons, megalodons, collossal_squid, blue_whales, sharks, mr_crabs, squids, shrimps, salmons, cods, multiplier
    return (type + type2) * price * multiplier


def first_discovery(x):
    newframe
    print(f"first discovery: {str(x)}")
    input("type anything to continue: ")


def check(chance):
    global fish
    if fish <= chance:
        return 1
    else:
        return 0


def newframe(x):
    if x >= 0:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def fishani(x):
    if x == 1:
        newframe(1)
        print("            ½½½½½½        00000\n          ½½½½½½½½½½   0000   L\n          ½½½½½½½½½½ 000       L\n            ½½½½½½  00          L\n         ½½½½½½½   00            9\n         ½½½½½½½½ 000\n        ½½½½½½½½½½0")
        time.sleep(0.5)
        newframe(1)
        print("            ½½½½½½        00000\n          ½½½½½½½½½½   0000   L\n          ½½½½½½½½½½ 000       L\n            ½½½½½½  00          L\n         ½½½½½½½   00            L\n         ½½½½½½½½ 000             L\n        ½½½½½½½½½½0                9")
        time.sleep(0.5)
        newframe(1)
        print("            ½½½½½½        00000\n          ½½½½½½½½½½   0000   |\n          ½½½½½½½½½½ 000      |\n            ½½½½½½  00        |\n         ½½½½½½½   00         |\n         ½½½½½½½½ 000         |\n        ½½½½½½½½½½0           9")
    if x == 2:
        newframe(1)
        print("            ½½½½½½        00000\n          ½½½½½½½½½½   0000   L\n          ½½½½½½½½½½ 000       L\n            ½½½½½½  00          L\n         ½½½½½½½   00            L\n         ½½½½½½½½ 000             L\n        ½½½½½½½½½½0                9")
        time.sleep(0.5)
        newframe(1)
        print("            ½½½½½½        00000\n          ½½½½½½½½½½   0000   |\n          ½½½½½½½½½½ 000      |\n            ½½½½½½  00        |\n         ½½½½½½½   00         |\n         ½½½½½½½½ 000         |\n        ½½½½½½½½½½0           9")
    if x == 3:
        newframe(1)
        print("            ½½½½½½        00000\n          ½½½½½½½½½½   0000   |\n          ½½½½½½½½½½ 000      |\n            ½½½½½½  00        |\n         ½½½½½½½   00         |\n         ½½½½½½½½ 000         |\n        ½½½½½½½½½½0           9")


def menu(x):
    global mortezas, sea_dragons, megalodons, collossal_squid, blue_whales, sharks, mr_crabs, old_boots, squids, shrimps, salmons, cods, money, goodrod, dragonbait, harpoon, megaharpoon, equicheck, rng_range, old_boats, normal_boats, big_boats, yachts, ships, whaling_ships, z, old, nor, big, yac, shi, wha
    if x == 2:
        print("fishing game stopped")

    elif x == 1:
        newframe(1)
        menu1 = input(f"Money: {money}\n\n1) go fishing (Enter)\n2) sell fish\n3) buy gear\n4) buy ships\n5) storage\n6) save progress\n7) quit\n\nchoose: ")

        if menu1 == "6":
            newframe(1)
            save(input("save:\n\n1) user 1          2) user 2          3) user 3\n\n\nchoose: "))
            menu(1)

        elif menu1 == "5":
            newframe(1)
            input(f"mortezas: {mortezas}\nsea dragons: {sea_dragons}\nmegalodons: {megalodons}\ncollossal squid: {collossal_squid}\nblue whales: {blue_whales}\n sharks: {sharks}\ncrabs: {mr_crabs}\nsquid: {squids} / shrimp: {shrimps}\nsalmon: {salmons} / cod: {cods}\nold boots: {old_boots}\n\ntype anything to go back to the menu: ")
            menu(1)

        elif menu1 == "4":
            newframe(1)
            boat_choice = input(f"boats:                              Money:{money}\n\n1) old boat(50.000)\n2) normal boat(125.000)\n3) big boat(300.000)\n4) yacht(1.000.000)\n5) ship(3.000.000)\n6) whaling ship(15.000.000)\n\nchoice: ")

            if boat_choice == "1":
                old = input("amount: ")
                errorfix(1, old)
                while old > 0 and quantity < 25:
                    if buy(old_boats, 50000, 2) == 1:
                        old_boats += 1
                    else:
                        old = 1
                    old -= 1

            elif boat_choice == "2":
                nor = input("amount: ")
                errorfix(1, nor)
                while nor > 0:
                    if buy(normal_boats, 125000, 2) == 1:
                        normal_boats += 1
                    else:
                        nor = 1
                    nor -= 1

            elif boat_choice == "3":
                big = input("amount: ")
                errorfix(1, big)
                while big > 0 and rng_range > 100000:
                    if buy(big_boats, 300000, 2) == 1:
                        big_boats += 1
                    else:
                        big = 1
                    big -= 1

            elif boat_choice == "4":
                yac = input("amount: ")
                errorfix(1, yac)
                while yac > 0:
                    if buy(yachts, 1000000, 2) == 1:
                        yachts += 1
                    else:
                        yac = 1
                    yac -= 1

            elif boat_choice == "5":
                shi = input("amount: ")
                errorfix(1, shi)
                while shi > 0:
                    if buy(ships, 3000000, 2) == 1:
                        ships += 1
                    else:
                        shi = 1
                    shi -= 1

            elif boat_choice == "6":
                wha = input("amount: ")
                errorfix(1, wha)
                while wha > 0 and diffquantity < [1] * 500:
                    if buy(whaling_ships, 15000000, 2) == 1:
                        whaling_ships += 1
                    else:
                        wha = 1
                    wha -= 1
            menu(1)

        elif menu1 == "3":
            newframe(1)
            buychoice = input(f"buy:                              Money:{money}\n\n1) good rod(15.000)\n2) dragon bait(50.000)\n3)harpoon(100.000)\n4) megaharpoon(1.250.000\n\nchoice: ")
            if buychoice == "1":
                if buy(goodrod, 15000, 1) == 1:
                    goodrod = True
                else:
                    print("not enough money")
                    time.sleep(1.5)
            elif buychoice == "2":
                if buy(dragonbait, 50000, 1) == 1:
                    dragonbait = True
                else:
                    print("not enough money")
            elif buychoice == "3":
                if buy(harpoon, 100000, 1) == 1:
                    harpoon = True
                else:
                    print("not enough money")
            elif buychoice == "4":
                if buy(megaharpoon, 1250000, 1) == 1:
                    megaharpoon = True
                else:
                    print("not enough money")
            menu(1)

        elif menu1 == "7":
            menu(2)

        elif menu1 == "2":
            newframe(1)
            sell_choice = input(f"sell:\n\n1)mortezas: {mortezas}\n2)sea dragons: {sea_dragons}\n3)megalodons: {megalodons}\n4)collossal squid: {collossal_squid}\n5)blue whales: {blue_whales}\n6)sharks: {sharks}\n7)crabs: {mr_crabs}\n8)squid: {squids} / shrimp: {shrimps}\n9)salmon: {salmons} / cod: {cods}\n\nyour choice (type nothing to exit)")
            if sell_choice == "1":
                money += sell(mortezas, 1000000000, 0)
                mortezas -= 1
            elif sell_choice == "2":
                money += sell(sea_dragons, 10000000, 0)
                sea_dragons -= 1
            elif sell_choice == "3":
                money += sell(megalodons, 1000000, 0)
                megalodons = 0
            elif sell_choice == "4":
                money += sell(collossal_squid, 500000, 0)
                collossal_squid = 0
            elif sell_choice == "5":
                money += sell(blue_whales, 45000, 0)
                blue_whales = 0
            elif sell_choice == "6":
                money += sell(sharks, 7500, 0)
                sharks = 0
            elif sell_choice == "7":
                money += sell(mr_crabs, 300, 0)
                mr_crabs = 0
            elif sell_choice == "8":
                money += sell(squids, 200, shrimps)
                squids = 0
                shrimps = 0
            elif sell_choice == "9":
                money += sell(salmons, 250, cods)
                salmons = 0
                cods = 0
            menu(1)

        elif menu1 == "1" or "\n":
            fishani(1)
            for z in diffquantity:
                global fish
                fish = random.randint(1, rng_range)
                global mor, cod, mrc, sea, blu, sal, meg, squ, col, shr, boot, sha
                mor_check = check(mor)
                sea_check = check(sea)
                meg_check = check(meg)
                col_check = check(col)
                blu_check = check(blu)
                sha_check = check(sha)
                mrc_check = check(mrc)
                old_check = check(boot)
                squ_check = check(squ)
                shr_check = check(shr)
                sal_check = check(sal)
                cod_check = check(cod)

                global a, b, c, d, e, f, g, h, i, j, k
                if mor_check == 1:
                    if mortezas <= 0.5 and a == 0:
                        first_discovery("morteza")
                        a = 1
                    mortezas += 1
                    print("you caught the legendary, great, leader of the ocean, Morteza!!!")
                    input("type anything to continue: ")

                elif sea_check == 1:
                    if sea_dragons <= 0.5 and b == 0:
                        first_discovery("sea_dragon")
                        b = 1
                    sea_dragons += 1
                    print("you caught the godly Seadragon!!!")
                    input("type anything to continue: ")

                elif meg_check == 1:
                    if megalodons <= 0.5 and c == 0:
                        first_discovery("megalodon")
                        c = 1
                    megalodons += 1
                    print("you harpooned a mithical Megalodon!")
                    input("type anything to continue: ")

                elif col_check == 1:
                    if collossal_squid <= 0.5 and d == 0:
                        first_discovery("collossal_squid")
                        d = 1
                    collossal_squid += 1 * quantity
                    if quantity >= 1:
                        print(f"{quantity} collossal squids")
                    else:
                        print("i didnt even knew this existed!, a collossal squid")
                    if diffquantity < [1] * 300:
                        input("type anything to continue: ")

                elif blu_check == 1:
                    if blue_whales <= 0.5 and e == 0:
                        first_discovery("blue_whale")
                        e = 1
                    blue_whales += 1 * quantity
                    if quantity >= 1:
                        print(f"{quantity} giant blue whales")
                    else:
                        print("a giant blue whale!")
                    if diffquantity < [1] * 200:
                        input("type anything to continue: ")

                elif sha_check == 1:
                    if sharks <= 0.5 and f == 0:
                        first_discovery("shark")
                        f = 1
                    sharks += 1 * quantity
                    if quantity >= 1:
                        print(f"{quantity} sharks, wow!")
                    else:
                        print("a shark")
                    if diffquantity < [1] * 100:
                        input("type anything to continue: ")

                elif mrc_check == 1:
                    if mr_crabs <= 0.5 and g == 0:
                        first_discovery("mr_crabs")
                        g = 1
                    mr_crabs += 1 * quantity
                    print("what is mr crabs doing here?")
                    if diffquantity < [1] * 50:
                        input("type anything to continue: ")

                elif old_check == 1:
                    old_boots += 1
                    print("an old boot...  :(")

                elif squ_check == 1:
                    if squids <= 0.5 and h == 0:
                        first_discovery("squid")
                        h = 1
                    squids += 1 * quantity
                    print(f"{quantity} squid")

                elif shr_check == 1:
                    if shrimps <= 0.5 and i == 0:
                        first_discovery("shrimp")
                        i = 1
                    shrimps += 1 * quantity
                    print(f"{quantity} shrimp")

                elif sal_check == 1:
                    if salmons <= 0.5 and j == 0:
                        first_discovery("salmon")
                        j = 1
                    salmons += 1 * quantity
                    print(f"{quantity} salmon")

                elif cod_check == 1:
                    if cods <= 0.5 and k == 0:
                        first_discovery("cod")
                        k = 1
                    cods += 1 * quantity
                    print(f"{quantity} cod")
                else:
                    print("oh, you didnt catch anything")
            time.sleep(0.8)
            menu1 = "0"
            menu(1)


def cat_script():
    time.sleep(600)
    newframe(1)


equi_thread = threading.Thread(daemon=True, target=equipment_check)

equi_thread.start()
newframe(1)
load(input("fishing game launched\n\nload(only if you saved as that user, otherwise enter to skip):\n\n1) user 1          2) user 2          3) user 3\n\n\nchoose: "))

menu(1)
