input_string = input()

cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 
            'nj', 's=', 'z=']

for i in cro_list:
    input_string = input_string.replace(i, "*")

print(len(input_string))