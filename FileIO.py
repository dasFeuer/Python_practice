f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# f = open('myfile.txt', 'rb')
# text = f.read()
# print(text)
# f.close()

# f = open('myfile.txt', 'a')
# f.write("Hello World")
# f.close()

# f = open('myfile.txt', 'w')
# f.write("Hello World")
# f.close()

with open('myfile.txt', 'a')as f:
    f.write("Hey I am a programmer.")

with open('myfile.txt', 'a')as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    data = f.read(5)
    print(data)

with open('myfile.txt', 'w')as f:
    f.write("Hello World!")
    f.truncate(3)

with open('myfile.txt', 'r')as f:
    print(f.read())
