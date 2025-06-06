import os

''' 1. -----  File and Directory Manipulation ------'''
# print(os.getcwd())
# # os.chdir("anything path")
# print(os.listdir())
# # os.mkdir("new_directory")
# # os.rmdir("new_directory")

# # remove a file 

# with open('text.txt','w') as f:
#     f.write('hello World!.')

# os.remove('text.txt')

''' 2. ----- Path Manipulation -------- '''
# print(os.path.exists('2.png'))

''' 3. ----- Running System Commands -------- '''


''' 3. ----- Another Type -------- '''

print(os.name)

print(os.sep)

# print(os.uname())

# os.makedirs()

# curr = os.getcwd()
# for direpath, dirname,filename in os.walk(curr):
#     print(filename)

# print(os.stat("1.ico"))

# cur = os.getcwd()
# new_floder = os.path.join(cur,"unique_program")
# file_name = os.path.join(new_floder,"anuj.txt")
# with open(file_name,'w') as f:
#     f.write("anuj is ond")

# print(os.path.exists("new_folder"))

curr = os.getcwd()
file_name = os.path.join(curr,"2.ico")
# print(os.path.split(file_name))
# print(os.path.splitext(file_name))
# rename is used to rename the file 
# os.rename(file_name,"2.ico")

unique_folder = os.path.join(curr,"unique_program")
# rename is used to cut and paste the file_name
# os.rename(f"{unique_folder}/2.ico",file_name)

# os.remove(os.path.join(unique_folder,"anuj.txt"))

# os.rmdir()  remove the external directory 
# os.removedirs() remove all tree directory

