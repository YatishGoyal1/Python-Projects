import os
def open_file(filename):
    try:
         with open(filename,"w") as file:
           print(f"{filename} Created Sucessfullty")
    except FileExistsError:
        print(FileExistsError)
    except Exception as E:
        print("An Error Occured")
def view_file():
        files = os.listdir()
        if not files:
            print("No File Found!")
        else:
            for file in files:
                print(files)
def delete_file(filename):
   try:
         os.remove(filename)
         print(f"{filename} Deleted Succesfully")
   except FileExistsError:
        print(FileExistsError)
   except Exception as E:
        print("An Error Occured")

    



       