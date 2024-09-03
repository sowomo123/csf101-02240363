with open("fruit_transactions.txt","r+") as file:
    data = file.readlines()

    length = len(data)
    print(f'the length of data is {length}')
