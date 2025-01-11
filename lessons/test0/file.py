import random

# file_name = 'f1.tx'
# file = open(file_name, mode='w')
#
# try:
#     for n in range(0, 10):
#         file.write('Text \n')
# finally:
#     file.close()


# file_name ='f2.txt'
# with open(file_name, 'w') as file:
#     for n in range(0, 100):
#         file.write(str(random.randint(0,10000))+'\n')


with open('f1.tx', 'r') as file:
        content = file.read()
        print(content)

with open('f1.tx', 'r') as file:
        line = file.readline()
        while line:
            print(line)

            line = file.readline()