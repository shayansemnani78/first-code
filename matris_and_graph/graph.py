file_name=input("pls enter your file name ")
input_info = open(file_name)
input_info = input_info.read()
input_info = input_info.splitlines()

vertex_numbers = int(input_info[0])
status = input_info[-1]
statused_vertex = input_info[-2]
del input_info[0]
del input_info[-1]
del input_info[-1]

# print(input_info)
# print(status)
# print(statused_vertex)
# print(vertex_numbers)