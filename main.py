from colorama import init, Fore
import goods_data
import cards_data


def choose_an_good():
    print('LIST OF GOODS: ')
    print(goods_data.goods_data1)
    try:
        good_number = int(input(Fore.YELLOW + 'ENTER A NUMBER OF PRODUCT TO BUY IT: \n'))
        if 0 < good_number < len(goods_data.goods_data1):
            return good_number
        else:
            print(Fore.RED + 'No items with this number. Try again.')
            choose_an_good()
    except ValueError:
        print(Fore.RED + 'Enter only numbers.')
        choose_an_good()


def cls(): print("\n" * 100)


def choose_a_card():
    print('LIST OF CARDS: ')
    print(cards_data.cards_data1.to_string(index=False))
    cards_number = input(Fore.YELLOW + 'CHOOSE A CARD\n(4 NUMBERS) : \n')
    if (cards_data.cards_data1.Number == cards_number).any():
        return cards_number
    else:
        print(Fore.RED + 'Enter 4 numbers of a card.')
        choose_a_card()


def balance_in_this_card(num):
    return (cards_data.cards_data1.loc[cards_data.cards_data1.Number == num]['Balance']).item()


def product_price(index):
    return (goods_data.goods_data1.loc[index]['Price']).item()


def checking_of_money(good_number, card_index):
    card_balance1 = balance_in_this_card(card_index)
    good_price1 = product_price(good_number)
    if card_balance1 >= good_price1:
        return True
    else:
        return False


def process_of_buying(good_index, card_index):
    print(Fore.LIGHTGREEN_EX + 'Well done!')
    print(Fore.GREEN + 'You bought: ' + str(goods_data.goods_data1.loc[good_index]['Item']))
    print(Fore.GREEN + 'Price: ' + str(goods_data.goods_data1.loc[good_index]['Price']) + ' PLN')
    print(Fore.GREEN + 'Card: ' + str(
        (cards_data.cards_data1.loc[cards_data.cards_data1.Number == card_index]['Name']).item()))
    print(Fore.LIGHTGREEN_EX + 'Thank You!')
    input(Fore.YELLOW + "Press Enter to continue...")
    cls()


def buy_good():
    good_number = choose_an_good()
    card_number = choose_a_card()
    if checking_of_money(good_number, card_number):
        process_of_buying(good_number, card_number)
    else:
        print(Fore.RED + 'It\'s not enough money on this card, choose another one and try again.')
        buy_good()


def category(num):
    return num


def selection(num):
    if num == 'y' or num == 'yes':
        return True
    elif num == 'n' or num == 'no':
        return False
    else:
        return False


def sell_good():
    name = input(Fore.YELLOW + 'NAME OF PRODUCT: \n')
    category1 = category(input(Fore.YELLOW + 'NUMBER OF CATEGORY: \n'))
    price = int(input(Fore.YELLOW + 'PRICE: '))
    selection1 = selection((input(Fore.YELLOW + 'ENTER Y OR N (YES/NO)...')).lower())
    goods_data.goods_data1.loc[len(goods_data.goods_data1)] = [name, category1, price, selection1]

    goods_data.goods_data1 = goods_data.goods_data1.sort_values(by='Selection', ascending=False)
    goods_data.goods_data1 = goods_data.goods_data1.reset_index(drop=True)
    goods_data.goods_data1.index = goods_data.goods_data1.index + 1

    print(goods_data.goods_data1)


if __name__ == '__main__':
    init(autoreset=True)
    while True:
        print('''CHOOSE AN OPTION:
        1 => BUY
        2 => SELL
        3 => EXIT''')
        x = input(Fore.YELLOW + 'PRESS 1, 2 OR 3: \n')
        if x == '1':
            buy_good()
        if x == '2':
            sell_good()
        if x == '3':
            break
