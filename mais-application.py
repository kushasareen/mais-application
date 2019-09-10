import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

loan_dict = defaultdict(dict)

# read relevant entries from files into a dictionary
with open(r'C:\Users\kusha\Desktop\loan_data.csv', mode='r') as csv_file: # enter file path here
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        loan_dict[f'{row["member_id"]}'][0] = f'{row["loan_amnt"]}'

with open(r'C:\Users\kusha\Desktop\home_ownership_data.csv', mode='r') as csv_file: # enter file path here
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        loan_dict[f'{row["member_id"]}'][1] = f'{row["home_ownership"]}'


# interate through dictionary and compute average
num_own = own_sum = num_mortgage = mortgage_sum = num_rent = rent_sum = 0
for key in loan_dict:
    if loan_dict[key][1] == 'OWN':
        num_own += 1
        own_sum += int(loan_dict[key][0])
    elif loan_dict[key][1] == 'MORTGAGE':
        num_mortgage += 1
        mortgage_sum += int(loan_dict[key][0])
    elif loan_dict[key][1] == 'RENT':
        num_rent += 1
        rent_sum += int(loan_dict[key][0])

mortgage_avg = mortgage_sum/num_mortgage
own_avg = own_sum/num_own
rent_avg = rent_sum/num_rent

# store averages in a list
avg = []
avg.append(mortgage_sum/num_mortgage)
avg.append(own_sum/num_own)
avg.append(rent_sum/num_rent)


# write averages to a csv file
with open(r'C:\Users\kusha\Desktop\average_loans.csv', mode='w', newline='') as csv_file: # enter file path here
    fieldnames = ['home_ownership', 'loan_amnt']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerow({'home_ownership': 'MORTGAGE', 'loan_amnt': avg[0]})
    csv_writer.writerow({'home_ownership': 'OWN', 'loan_amnt': avg[1]})
    csv_writer.writerow({'home_ownership': 'RENT', 'loan_amnt': avg[2]})

label = ['MORTGAGE', 'OWN', 'RENT']


# plots a bar graph with respective averages and home ownerships
def plot_bar():
    index = np.arange(len(label))
    plt.bar(index, avg)
    plt.xlabel('Home Ownership')
    plt.ylabel('Average Loan Amount ($)')
    plt.xticks(index, label)
    plt.title('Average loan amounts per home ownership')
    plt.show()


plot_bar()
