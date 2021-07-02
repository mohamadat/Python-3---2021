
import random as r;



def main():
    # user keep choosing the magical number(1-10) untill he find it, he wins
    ci = r.randint(0, 11);

    while True:
        ui = int(input("Please enter number [1-10]"));
        if ui == ci:
            print('you win :) ');
            input = input('To try againg press \'y\' ')
            if input == 'y':
                pass;
           
            break;

main();