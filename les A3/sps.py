import random;


# Steen, schaar, papier

def play():
    # 1- users input
    user_input = input("""Please choose, 's' voor steen,
    'sch' voor schaar,
    'p' voor papier
    """);

    
    # 2- computer input ??
    choises = ["s","p","sch"];
    computer_input = random.choice(choises);

    # 3- logic compare the winner
    # 4- notify the answer
    x = is_winner(user_input, computer_input);
    print("computer input was ", computer_input );
    if(x):
        print(" You win, Heeeeee!");
    else:
        print("You lose :(");








#  schaar > papier > steen
# 3- logic compare the winner
def is_winner(ui, ci):
    if (ui == 'sch' and ci == 'p') or (ui == 'p' and ci == 's') or (ui == 's' and ci == 'sch'):
        return True
    return False;

while(True):
    play();
