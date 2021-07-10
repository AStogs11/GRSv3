import os
 

#list all files in a dir using os.listdir

#set path to all of your stuffz
DropFolder = 'C:\Users\Alex\Desktop\Handicap_data\Drop\\'
DataFolder = 'C:\Users\Alex\Desktop\Handicap_data\Data\\'
ArchiveFolder = 'C:\Users\Alex\Desktop\Handicap_data\Archive\\'



def my_unzip(zip_filename):
    print "Unzipping ", zip_filename
    import zipfile
    zip_ref = zipfile.ZipFile(DropFolder + zip_filename, 'r')
    zip_ref.extractall(DataFolder)
    print "File Sucessfully Unzipped and Moved to Data Folder"
    zip_ref.close()

def check_for_zips(DataFolder):
    import fnmatch
    for file_name in os.listdir(DropFolder):
        if fnmatch.fnmatch(file_name, '*.zip'):
            print(file_name)
            print "Creating Backup and moving to Backup Folder"
            my_unzip(file_name)
            os.rename(DropFolder + file_name, ArchiveFolder + file_name)
            print "Backup sucessfully created"
               

def main():
    check_for_zips(DropFolder)
    import time
    time.sleep(5)
    print "Waiting for dat Horse Data- Once Imported, you can close"
    

os._exit
main()



