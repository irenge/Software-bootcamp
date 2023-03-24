def min(x):
    z = x[0]
    for i in x:
        if z > i:
            z = i
    return z

def max(x):
    z = x[0]
    for i in x:
        if z < i:
            z = i
    return z

def avg(x):
    s = 0.0
    c = 0
    for i in x:
        c += 1.0
        s += i
    avg = s / c
    return avg

print(min([2,3,4]))
print(max([4,5,7]))
print(len([2,3,4]))



f = open("input.txt", "r", encoding='utf-8-sig')
lines = f.read()
print(lines)
print(type(lines))
lines = lines.split('\n')
while '' in lines:
    lines.remove('')
print(lines)
txt = open("output.txt", "w")

for line in lines:
    line = line.split(':')
    #line[1] = line[1].strip('\n')
    print(line)
    line[1] = line[1].split(',')
    line[1] = [eval(i) for i in line[1]]
    #print (line)
    if line[0] == 'min':
        txt.write(f'\nThe min of {line[1]} is {min(line[1])}')
        print(f'The min of {line[1]} is {min(line[1])}')
    elif line[0] == 'max':
        txt.write(f'\nThe max of {line[1]} is {max(line[1])}')
        print(f'The max of {line[1]} is {max(line[1])}')

    else:
        txt.write(f'\nThe avg of {line[1]} is {avg(line[1])}\n')
        print(f'The avg of {line[1]} is {avg(line[1])}')

