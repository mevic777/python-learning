import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    # result = [random.choice(symbols) for _ in range(3)] # _ is just a placeholder for iteration
    # return result

    # OR

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" ".join(row)) # joining the string with a space

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    else:
        return 0

def main():
    balance = 100

    print("Welcome to the slot machine !")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
        
        if bet <= 0:
            print("Negative bet")
            continue

        balance -= bet

        row = spin_row()

        print_row(row)

        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print(f"Sorry you lost this round")
        
        balance += payout

        play_again = input("Do you want to spin again? (y/n): ").upper()

        if play_again != 'Y':
            break

    print(f"Game over, your current balance is ${balance}")

if __name__ == "__main__":
    main()