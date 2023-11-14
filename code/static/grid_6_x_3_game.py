# Importing the random library for generating the random numbers
import random
import string


# Select the roman numbers
def draw_random_number():

    # List to store the all the generated random numbers
    random_list = []

    # First drawn number:whole number
    first = random.randint(1, 25)
    random_list.append(first)

    # Second drawn number:factor of the first drawn number
    factors = []
    for i in range(1, random_list[0]+1):
        if random_list[0] % i == 0:
            factors.append(i)
    # Selecting the random number from the factors list
    second = random.choice(factors)
    random_list.append(second)

    # Third drawn number:multiple of first and second drawn numbers
    thrid = random_list[0]*random_list[1]
    random_list.append(thrid)

    # Forth drawn number:any number
    random_list.append(random.randint(1, 1326))

    # Sixth number :any number
    sixth = random.randint(1, 1326)
    random_list.append(sixth)

    # Fifth drawn number :smallest among all the numbers that are in the random_list
    random_list.insert(4, min(random_list))

    return random_list


# function to convert the number to roman
def roman_conversion(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    symbols = ["I", "IV", "V", "IX", "X", "XL",
               "L", "XC", "C", "CD", "D", "CM", "M"]
    index = 12
    result = ''
    while number:
        div = number // num[index]
        number %= num[index]

        while div:
            result += symbols[index]
            div -= 1
        index -= 1
    return result


# Generate the strip
def generate_strip():
    grid = []

    # First Strip for only uppercase english alphabets
    first_strip = list(string.ascii_uppercase)

    # Second Strip for only lowercase english alphabets
    second_strip = list(string.ascii_lowercase)

    # Iterating for 3 rows
    for i in range(3):
        numbers = draw_random_number()
        index0 = numbers[0]  # first strip
        index1 = numbers[1]  # second strip
        index4 = numbers[4]  # fifth strip
        index5 = numbers[5]  # sixth strip
        first_strip_symbols = first_strip[index0]
        second_strip_symbols = second_strip[index1]
        # combination of any two alphabets
        forth_strip_symbols = ''.join(random.sample(
            string.ascii_letters, 2))  # forth strip
        fifth_strip_symbols = roman_conversion(
            index4)  # smallest roman numbers among all
        sixth_strip_symbols = roman_conversion(index5)  # any roman number
        # adding all symbols to the grid list
        grid.extend(first_strip_symbols)
        grid.extend(second_strip_symbols)
        grid.extend(forth_strip_symbols)
        grid.append(fifth_strip_symbols)
        grid.append(sixth_strip_symbols)

    # Third Strip Greek alphabets
    third_strip = [chr(i) for i in range(945, 970)]

    # Iterating for 3 rows
    count = 0
    while count < 3:
        numbers = draw_random_number()
        index2 = numbers[2]
        if index2 < 25:
            count += 1
            third_strip_symbols = third_strip[index2]
            grid.extend(third_strip_symbols)

    return grid


# Combine all strips elements into one list of length 108
def generate_strip_combination():
    final_grid = []
    while len(final_grid) < 100:
        final_grid.extend(generate_strip())
    return final_grid


# Selecting random element from the strips 
def create_grid_from_combination():
    grid = []

    strips = generate_strip_combination()
    for i in range(6):
        grid.append(random.sample(strips, 3))
    return grid


# Convert grid into specific format
def grid_conversion_to_specific_format():
    # Converting the grid of 3x6 to 6x3 by transposing the matrix
    grid = create_grid_from_combination()
    complete_grid = [[grid[j][i]
                      for j in range(len(grid))] for i in range(len(grid[0]))]
    return complete_grid


# Calculate the winning in the grid
def calculate_winnings(grid):
    winnings = 0
    counts = {}
    # winning for first symbol is 2 and follow up symbols pay twice the pervious one
    win = {0: 2, 1: 4, 2: 8}
    # calculate count of symbol and repetation of symbol in 3x6
    for strip in grid:
        for i in range(len(strip)):
            symbol = grid[0][i]  # taking only first strip symbols
            # count number of symbols in each strip
            symbol_count = strip.count(symbol)
            if symbol_count != 0:
                if symbol not in counts:
                    counts[symbol] = {}
                    counts[symbol]['count'] = strip.count(symbol)
                    counts[symbol]['multiplier'] = strip.count(
                        symbol)  # if same symbol repeat in same strip
                else:
                    counts[symbol]['count'] += strip.count(symbol)
                    counts[symbol]['multiplier'] *= strip.count(symbol)

    # calculate the win as per the count and repetation of symbol
    for i in range(len(grid[0])):
        symbol = grid[0][i]
        if counts[symbol]['count'] == 6:
            winnings += win[i]
        if counts[symbol]['count'] > 6:
            winnings += win[i] * counts[symbol]['multiplier']
            print('winnings, symbol',winnings, symbol)
    print('strip', strip)
    print('counts',counts)
    return winnings


# Start the game
def start_game():
    grid = create_grid_from_combination()  # creating grid
    print(grid)
    winnings = calculate_winnings(grid)  # calculating win
    final_grid = grid_conversion_to_specific_format()  # grid to be shown in UI
    for row in final_grid:
        print(row)
    print("Total Winnings:", winnings)
    final = [final_grid, winnings]  # to pass the data to FE
    print('final', final)
    return final
