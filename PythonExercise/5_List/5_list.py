# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,                
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expense = [2200,2350,2600,2130,2190]
print(expense)

print("More amount spent in Feb Compared to Jan is ", expense[1]-expense[0])
print("Total expense in the first quarter is :", expense[1]+expense[0]+expense[2])
print("did u spend in 200$ in any month :", 2000 in expense)

# append June month expense 
expense.append(1980)
print(expense)

# Correction for April month 
expense[3] = expense[3] - 200
print("Correction for April month :", expense)


# Excercise 2 
# 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.pop()
heros.insert(3, 'black panther')
print(heros)
heros[1:3] = ['docker strange']
print(heros)

print(dir(heros))
heros.sort()
print(heros)