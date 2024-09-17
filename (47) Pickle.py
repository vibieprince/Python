import pickle
l=[10,20,30,40,50]
file=open("checking.txt","wb")
pickle.dump(l,file)
file.close()

file=open("checking.txt","rb")
l=pickle.load(file)
print(l)