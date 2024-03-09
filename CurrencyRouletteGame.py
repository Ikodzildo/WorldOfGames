from forex_python.converter import CurrencyRates


# def get_exchange_rate():
#     c = CurrencyRates()
#     exchange_rate = c.get_rate('USD', 'ILS')
#     return exchange_rate
#
# usd_to_ils_rate = get_exchange_rate()
# print(f'USD to ILS exchange rate: {usd_to_ils_rate}')

def play(difficulty):
    get_money_interval1 = get_money_interval(difficulty)
    guess_from_user1 = get_guess_from_user()
    if get_money_interval1 == guess_from_user1:
        return True
    else:
        return False


def get_money_interval(difficulty):
    d = difficulty
    print(f'choose amount of money')
    amount_of_money_from_user = int(input())
    t = amount_of_money_from_user
    return (t - (5 - d), t + (5 - d))


def get_guess_from_user():
    print(f'Guess how many ILS for a the amount of Dollars')
    guess_from_user1 = int(input())
    return guess_from_user1
