my_list.append('30')
my_list.append('40')
#add value at the second last position
my_list.insert(1,'15')
#extend my list with another list
my_list.extend(['50','60','70'])
#remove the last element from my list
my_list.pop(-1)
#sorting the values in my list in ascending order
my_list.sort()
#find and print the index of value of 30 in my list
index_30 = my_list.index('30')
print("index of 30:",index_30)
print(my_list)