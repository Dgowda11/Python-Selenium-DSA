my_list = [1, 2, 3, 4, 5]

# App1
my_list[0],my_list[-1] = my_list[-1],my_list[0]
print(my_list)

def swap(my_list):
    size  = len(my_list)
    temp = my_list[0]
    my_list[0] = my_list[size-1]
    my_list[size -1]  = temp

    return my_list
print(swap(my_list=my_list))
