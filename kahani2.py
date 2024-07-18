kahani = ""
while True:
    data= input("Enter the Story:")
    if len(data)==0:
        print("The end!")
        break
    kahani += data +"\n"

with open("story.txt","w")as file:
    file.write(kahani)