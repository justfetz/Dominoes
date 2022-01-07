import random


full_domino_set = [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [2,2],\
                   [2,3], [2,4], [2,5], [2,6], [3,3], [3,4], [3,5],\
                   [3,6], [4,4], [4,5], [4,6], [5,5], [5,6], [6,6],\
                   [0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6]]

stock_pieces = []
computer_pieces = []
player_pieces = []
domino_snake = 0
status = ""

def shuffle_deck(domino_set = []):
    return random.shuffle(domino_set)

def determine_if_start_exists():
    return 0

def fill_stock():
    j = 0
    while j < 14:
        domino = full_domino_set[random.randint(0, len(full_domino_set)-1)]
        print(domino)
        stock_pieces.append(domino)
        full_domino_set.remove(domino)
        j += 1

def fill_comp():
    k = 0
    while k < 7:
        computer_domino = full_domino_set[random.randint(0, len(full_domino_set)-1)]
        #print(domino)
        computer_pieces.append(computer_domino)
        full_domino_set.remove(computer_domino)
        k += 1

def fill_player():
    l = 0
    while l < 7:
        player_domino = full_domino_set[random.randint(0, len(full_domino_set)-1)]
        #print(domino)
        player_pieces.append(player_domino)
        full_domino_set.remove(player_domino)
        l += 1

fill_stock()
fill_comp()
fill_player()

print("Stock pieces:\n----------")
print(stock_pieces)

print("Player pieces:\n---------")
print(player_pieces)

print("Computer pieces:\n---------")
print(computer_pieces)

#determine starting player

#determine domino snake

#reset board if there is no starter

