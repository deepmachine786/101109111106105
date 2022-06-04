import os 


# create a all folder to get acces or store all images in the current _folder ..
def create_directory(lists: list):
    try:
        for i in lists:
            if i not in os.getcwd():
                os.mkdir(i)
            else: 
                print(" folder is already created ..")
                continue
    except Exception as e:
        print(" Unsuccefully Created Folder ..", e)
        exit(0) # if t he eror is occured then it is exit ..