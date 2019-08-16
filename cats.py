#  Lists 

# name = 'zelda'
# level = 5
# awesomeness = 95.5
# is_raining = True

# backpack = []

# backpack = ['drink bottle', 'yoghurt','headphones','candy']

# print(backpack)

# backpack.append('blueberries')
# backpack.append('book')
# backpack.append('python')
# print(backpack)

# print()

# print(backpack[0]) 

# # print(backpack[0]) ='lunchbox' 
# print(backpack)

# print()
# name = 'zelda'
# # print(name[0])
# # name[0] = 'c'
# # print(name)  # not working

# print(backpack)

# for index,item in enumerate(backpack) : 
#     print(index,item)

# print()

# counter = 0 
# for item in backpack : 
#         print(counter, item)
#         counter = counter +1

# counter = 0
# while counter < len(backpack):
#     print(counter, backpack[counter])
#     counter = counter +1  


# lists = [1,2,3,4,5,6,7,8,9,10]

# print(lists)


x = range (10)

counter = 1
for n in x:

    print(n+1)

counter = 1
while counter < len(x):
    print(counter, x[counter])
    counter = counter +1  

# print('number')
# for num in range(1,11)
# print(num)

# print()
# print('while loop')
# num = 1
# while num <= 10:
#     print(num)
#     num+=1

# Tuples 

# person = ('zelda','jack')
# print(person)
# person[0] = 'lj'

# def cats():
#     return('boris','larry',name)

## TASK 2
​
# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user
​
five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]
​
# first step is to add colum 6 and row 6
​
# output the grid to the user
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)
​
# output the grid with the flipped card
​
## TASK 2
​
# given a six by six grid, work out what card was flipped
​
# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)