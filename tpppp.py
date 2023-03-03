# with open("texting.txt",'r') as data_file:
#     for line in data_file:
#         data = line.split()
#         print(data) 

with open("texting.txt",'r') as file:
    lines = file.readlines()

with open("romeo_A.txt",'w') as file:
    for line in lines[:int(len(lines)/2 )]:
        file.write(line)

with open("romeo_B.txt",'w') as file:
    for line in lines[int(len(lines)/2):]:
        file.write(line)