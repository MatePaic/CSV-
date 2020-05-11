with open('zadaca.csv', 'r') as csv_file:
    items = csv_file.read().split()
    tina = items[1][0:4]
    jakob = items[2][0:5]
    barbara = items[3][0:7]

    female = items [1] [8:14]
    male = items [2][9:13]

    twenty_three = items[1][5:7]
    thirty_five = items[2][6:8]
    fourty_four = items[3][8:10]


    print(f'{tina} is {female} and {twenty_three} years old')
    print(f'{jakob} is {male} and {thirty_five} years old')
    print(f'{barbara} is {female} and {fourty_four} years old')