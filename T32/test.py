f = open ("test.txt", "r")
#bline = f.readlines()[:1]
#print (bline)
lines = f.readlines()[1:]
print(lines)
print("======================")
i = 0
for line in lines:
    line = line.strip().split(",")
    line[3] = int(line[3])
    line[4] = int(line[4])
    print(f"{i}: {line}")
    i += 1
    
    if i == 10:
        line[4] = 888
        lines[10] = f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]}\n"
        
g = open("simple.txt", "w")
g.writelines(lines)
g.close()

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

x = Point(2,3)
print(x)
