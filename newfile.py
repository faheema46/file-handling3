try:
    with open("file.txt","r") as file:
        content=file.read()
        len=0
        for char in content:
            if(char!=" "):
                len+=1
        print(len)

except FileNotFounderror:
  print("The file was not found")
except Eception as e:
  print("An error occured",e)       