#testing 

pizzas=['marinara', 'margheritta', 'napoletana', 'bianca', 'roma', 'chicago', 'ny pizza']

for pizza in pizzas:
    print('i like', pizza, 'pizza very much \n' )

print('pizza is the only meal that has changed my life')

numbers = list(range(0, 1001))

squares =[]

for k, number in enumerate(numbers):
    square = number**2
    print(k, square)
    squares.append(square)