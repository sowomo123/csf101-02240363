with open('basics/challenge-ex/fruit_transactions.txt', 'r') as file:
    data = file.readlines()

length = len(data)
print(f'The length of this data is {length}')

first_line = data[0]
print(f'The first line is: {first_line}')

all_dict_data = []
for line in data:
    line_dictionary = {}
    cleaned_line = line.replace('\n', '')
    splitted_line = cleaned_line.split(',')

    line_dictionary['name'] = splitted_line[0]
    line_dictionary['action'] = splitted_line[1]
    line_dictionary['quantity'] = int(splitted_line[2])
    line_dictionary['item'] = splitted_line[3]
    line_dictionary['price'] = float(splitted_line[4])

    all_dict_data.append(line_dictionary)

total_sales = sum(item['quantity'] * item['price'] for item in all_dict_data if item['action'] == 'sold')
print(f'Total sales from  sold transactions: ${total_sales}')

fruit_count = {}
for item in all_dict_data:
    fruit = item['item']
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1

most_popular_fruit = max(fruit_count, key=fruit_count.get)
most_popular_fruit_count = fruit_count[most_popular_fruit]

print(f'The most popular fruit is: {most_popular_fruit} with {most_popular_fruit_count} transactions')

total_value = sum(item['quantity'] * item['price'] for item in all_dict_data)
total_transactions = len(all_dict_data)
average = total_value / total_transactions
print(f'The average transaction value: {average:.2f}')

spender = {}
for item in all_dict_data:
    if item['action'] == 'bought':
        if item['name'] in spender:
            spender[item['name']] += item['quantity'] * item['price']
        else:
            spender[item['name']] = item['quantity'] * item['price']

biggest_spender = max(spender, key=spender.get)
total_amount = spender[biggest_spender]
print(f'Biggest spender is: {biggest_spender} with ${total_amount:.2f}')

summary = (
    f'Total sales: ${total_sales}\n'
    f'Popular fruit: {most_popular_fruit}\n'
    f'Average value: {average}\n'
    f'Biggest spender: {biggest_spender}\n'
)

with open('transaction_summary.txt', 'w') as summary_file:
    summary_file.write(summary)

print(f"The summary has been written in 'transaction_summary.txt'.")
