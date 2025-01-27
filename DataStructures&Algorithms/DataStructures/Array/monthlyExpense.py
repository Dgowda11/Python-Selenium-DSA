

exp = [2200,2350,2600,2130,2190]


# 1. In Feb, how many dollars you spent extra compare to January?
print("In Feb, how many dollars you spent extra compare to January?",exp[1]-exp[0])


# Find out your total expense in first quarter (first three months) of the year.
print("Total Expense in the first quarter is :", exp[0]+exp[1]+exp[2])

#  Find out if you spent exactly 2000 dollars in any month
print(2000 in exp)

exp.append(1980)
print("Expenses at the end of June:",exp) # [2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp) # [2200, 2350, 2600, 1930, 2190, 1980]