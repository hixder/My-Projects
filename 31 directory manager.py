import os

print("                               - ----> DIRECTORTY                                           ")
print("                                            MANAGER <------                                 ")

while(1):
    print("\n")
    print("Press 1 for knowing your present directory  :")
    print("Press 2 for changing your directory   :")
    print("Press 3 for displaying all the files of that directory  :")
    print("Press 4 for displaying folders of specific location  :")
    print("Press 5 for making  folder in that directory  :")
    print("Press 6 for renaming a file  :")
    print("Press 7 to check if a directory is present or not  :")
    print("Press 8 to check if a file is present in your directory  :")
    print("press 9 for EXIT  :")
    print("\n")


    choice=int(input("Enter the choice"))


    if(choice==1):
        try:
            print(os.getcwd())
            print("TASK COMPLETED\n")
        except Exception as th:
            print(th)
            continue


    elif(choice==2):
        try:
            address=input("enter the  new directory address")
            os.chdir(address)
            print("DIRECTORY CHANGED \n")
        except Exception as th:
            print(th)
            continue



    elif(choice == 3):
        try:
            print(os.listdir())
            print("TASK COMPLETED \n")
        except Exception as th:
            print(th)
            continue


    elif(choice == 4):
        try:
            address = input("enter the  new directory address")
            print(os.listdir(address))
            print("TASK COMPLETED\n")
        except Exception as th:
            print(th)
            continue


    elif(choice == 5):
        try:

            name=input("enter the folder name")
            os.mkdir(name)
            print("FOLDER CREATED \n")
        except Exception as th:
            print(th)
            continue


    elif(choice == 6):
        try:
            previous=input("input previous file name")
            new=input("new file name")
            os.rename(previous, new)
            print("UPDATED, open again if not visible  \n")

        except Exception as th:
            print(th)
            continue


    elif(choice==7):
        try:
            address=input("enter the directory address")
            a=(os.path.exists(address))
            if a==1:
                print("IT IS PRESENT \n")
            else:
                print("IT IS NOT PRESENT \n")

        except Exception as th:
            print(th)
            continue

    elif (choice == 8):
        try:
            address = input("enter the file name")
            a=(os.path.isfile(address))
            if a==1:
                print("IT IS PRESENT \n")
            else:
                print("IT IS NOT PRESENT \n")

        except Exception as th:
            print(th)
            continue

    elif(choice==9):
        quit(9)


    else:
        print("you entered a wrong input")
        print("\n")
        continue

