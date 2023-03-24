import random

# Create a text file called numbers1.txt that contains Integers which are sorted from smallest to largest.

f = open("numbers1.txt", "w+")
numbers1 = sorted(random.sample(range(0, 1000), 10))
print(numbers1)
numbers1= list(map(str, numbers1))
f.write(' '.join(numbers1))
f.close()

# Create a text file called numbers1.txt that contains Integers which are sorted from smallest to largest.

g = open("numbers2.txt", "w+")
numbers2 = sorted(random.sample(range(0, 1000), 10))
numbers2 = list(map(str, numbers2))
g.write(' '.join(numbers2))
g.close()


f = open("numbers1.txt", "r")
g = open("numbers2.txt", "r")

a = open("all_numbers.txt", "w")


lines = f.readlines()
w = lines[0].split(',')
x = w[0].split(' ')

line = g.readlines()
y = line[0].split(',')
z = y[0].split(' ')


aa = x + z
res = [eval(i) for i in aa]
res = sorted(res)

res = list(map(str, res))
a.write(' '.join(res))

f.close()
g.close()
a.close()
