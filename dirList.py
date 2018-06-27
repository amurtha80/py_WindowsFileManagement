## This code produces a recursive directory file listing for the target
## file path

# libraries for folder/file methods and for conversion to date format
import os, time

## Note: "\" signals an escape sequence, so a double \ is needed to take a lieral
## single \

## first pass for folder

# starting directory
start_path = '\\\\top_level\\your_file_path_here\\' 

# print the path to the console that will be mined for the directory file list
print ("start_path: " , start_path)

# while the file is open, print the following header names to the first row:
#   Function, Owner_Folder, Directory, File_Name, File_Size, Mod_Date,
#   Create_Date
# insert commas between each header value as this is a *.csv file
with open('\\\\top_level\\your_file_path_here\\fileListTest.csv', 'w') as f:
    print("Function" + "," + "Owner_Folder" + "," + "Directory" +
          "," + "File_Name" + "," + "File_Size" + "," + "File_Owner" +
          "," + "Mod_Date" + "," + "Create_Date" + "\n", file=f, end='')

    # for loop to recursively navigate through all files within the directory
    # listing (recursively)
    for path,dirs,files in os.walk(start_path):
        for filename in files:
            fullFileName = path + '\\' + filename
            # obtain the length of the start_path
            subDir = path[len(start_path):]
            # return the position of the end slash for the sub directory
            endSlash = subDir.find('\\', 3)
            # if no ending slash, then take full subDir text minus
            # beginning slash
            if endSlash == -1 :  
               endSlash = len(subDir)  
            # from position 0 to char before 2nd slash (fixed as of 2018-05-02)
            ownerFolder = subDir[0:endSlash] 
            if ownerFolder == 'AAA_Housecleaning - to be deleted' :
                continue
            lenFullFileName = len(fullFileName)
            if lenFullFileName > 259 : # record entry if path is too long for obtaining stats
            #    print(ownerFolder + "," + subDir + "," + filename + "," + "0" + "," + "12/31/9999" + "," + "12/31/9999" + "," + "Path too long" + "\n", file=f, end='')
                continue
            try: fileStats = os.stat(fullFileName)
            except:
                print ("exception for: " , fullFileName)
                continue
            fileOwner = fileStats.st_uid
            createDate = time.strftime('%m/%d/%Y', time.gmtime(fileStats.st_ctime))
            modDate = time.strftime('%m/%d/%Y', time.gmtime(fileStats.st_mtime))
            
            # fixed filename variable by adding quotes to string so that commas
            # are preserved in the filename and not treated as a parsing
            # character for *.csv files (fixed as of 2018-05-02)
            if fileStats.st_size < 20000000 : # only print files < ~20MB
                print("Category" + "," + ownerFolder + "," + subDir + "," + "\"" +
                      filename + "\"" + "," + str(fileStats.st_size/1000000) + "," +
                      str(fileOwner) + "," + modDate + "," + createDate + "\n",
                      file=f, end='')

# Finished processing; close the file
f.close()    

# Alert user running the program that the processing has completed
print ("processing complete")

# can we add permissions to the script???  Would like to identify any folder where there are
# individual users and not a group as a whole
