def print_geometric_progression(a, r, n):
    current_value = a

    for i in range(n):
        print(current_value, end=' ')
        current_value = current_value * r


a = int(input('Enter the first element: '))
r = int(input('Enter the common ratio: '))
n = int(input('Enter total numbers to print: '))

print_geometric_progression(a, r, n)
