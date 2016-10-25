import os

# fout = open('output.txt', 'w')             #? w is for write

# line_1 = "How many roads must a man walk down \n"

# fout.write(line_1)

# line_2 = "Before you call him a man?\n"
# fout.write(line_2)

# fout.close()


# print(os.path.exists('output.txt'))         #?

# print(os.path.isdir('exercises'))          #?

# def walk2(dirname):
#     """Prints the name of all files in
#     dirname and its subdirectories.
    
#     dirname: strong name of directory
#     """
#     count = 0
#     for root, dirs, files in os.walk(dirname):
#         for filename in files:
#             print(os.path.join(root,filename))
#             count += 1
#     print(count, 'files in total.')

# walk2(os.getcwd())

try:
    fin = open('bad_file')              # fin = file in
except:
    print('Something went wrong.')
print('still works here.')