import pickle

# # Pickel is used to store data types value in a file 
# l = [10,30,40,50]
# # how to Write data in value in a file 
# file = open("writdata.txt","wb")

# pickle.dump(l,file)

# file.close()

file = open("writdata.txt","rb")

l = pickle.load(file)
print(l)