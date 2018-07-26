from core import *
from disk import *


def greet():
    print('''                       Welcome to 
                  Farspace Rental Company!
The space themed vehicle rental company that reaches for the stars.''')


def show_what_to_rent():
    print('''For Rent:
1 - Medium Spaceship: 
    To rent $5,000 a month
    Deposit $1,000
2 - Podracer:
    To rent $1000 for 5 days
    Deposit $500
3 - Space Invader:
    To rent $4,000 for a week
    Deposit $800
4 - Star Destroyer:
    To rent $10,000 for 2 weeks
    Deposit $10,000''')


def main():
    greet()
    show_what_to_rent()


if __name__ == '__main__':
    main()
