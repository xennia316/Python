a = float(input('First value: '))
b = float(input('Second value: '))
op = input('Operation(sum/sub/mul/div)')

match op:
    case 'sum':
        print(f'a + b = {a + b}')

    case 'sub':
        print(f'a - b = {a - b}')

    case 'mul':
        print(f'a *  b = {a * b}')

    case 'div':
        print(f'a / b = {a / b}')

    case _:
        print('Invalid')
