# with open("file.txt","r")as f1:
#     data=f1.readlines()
   
    
# for line in data:
#     word=line.split()
    
#     print(len(word))
    
    

# f1.close()

try:
   with open("file.txt","r")as f2:
    content=f2.read()
    

    print(len(content))
except FileNotFounderror:
  print("The file was not found")
except Eception as e:
  print("An error occured",e)

