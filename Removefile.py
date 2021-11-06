# importing the required modules
import time
import os
import shutil

# main function
def main():

     
     # initializing the count
     deleted_folders_count= 0
     deleted_file_count = 0

     # specify a path
     path = "/PATH_TO_DELETE"

     # specify a date
     days = 30

     # converting days to second
     # time.time() returns current time in second
     second = time.time() - (days * 24 * 60 * 60 )

     # checking whether the file is present in the path or not
     if os.path.exists(path):

         # iterating over each and every folder and file in the path
         for root_folder, folders, file in os.walk(path):

          # comparing the days
          if second >= get_file_or_folder_age(root_folder):

              # removing the file
              remove_folder(root_folder)
              deleted_folders_count += 1 #incrementing count

              # breaking after removing the root_folder
              break

          else:

                # checking folder from the root_folder
                for folder in folders:

                    # folder path
                    folder_path = os.path.join(root_folder, folder)

                    # comparing with the days
                    if second >= get_file_or_folder_age(folder_path):

                        # invoking the remove_file function
                        remove_file(path)
                        deleted_file_count +=1 # incrementing count

     else:

         # file/folder is not fount
         print(f'"{path}" is not found')
         deleted_file_count +=1 # incrementing count
       

     print(f"Total folders deleted: {deleted_folders_count}")
     print(f"Total file deleted: {deleted_file_count}")

def remove_folder(path):

    # removing the folder
    if not shutil.rmtree(path):

        #sucess message
        print(f"{path} is removed sucessfully")

    else:

        # failed message
        print(f"unable to delete the "+path)

def remove_file(path):

     # removing the file
     if not os.remove(path):

        #sucess message
        print(f"{path} is removed sucessfully")

     else:

        # failed message
        print(f"unable to delete the "+path)


def get_file_or_folder_age(path):

    # getting ctime of the file/folder
    # time will be in second
    ctime = os.stat(path).st_ctime

    # returing the time
    return ctime

if __name__ == '__main__':
    main()





         