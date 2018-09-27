import random
def hangman():
    word_list = ["cat","dog","capital","override","polymorphism","encapsulation","fuck"]
    word = word_list[random.randint(0,6)]
    wrong = 0
    stages = ["",
              "________         ",
              "|                ",
              "|        |       ",
              "|        0       ",
              "|       /|\      ",
              "|       /  \     ",
              "|                "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman! ")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "input one char:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters [cind] = '$'
        else:
            wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You won!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print("You lost! The answer is {}.".format(word))
hangman()
