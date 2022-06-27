
import os

def countfiles (folders):
    numfiles = 0
    ## ---Scan filesystem for dirs and files from specified folders--- ##
    for rootpath, dirlist, filelist in os.walk(folders):
        ## ---List of files found (filelist) in file system--- ##
        for eachfile in filelist:
            numfiles += 1
            os.path.join(rootpath, eachfile)
        ## ---List of directories found (dirlist) in file system--- ##
#        for eachdir in dirlist:
#            print(os.path.join(rootpath, eachdir))
#            numfiles += 1
#            fullpath = os.path.join(orig_drive + folders)
#            print (fullpath)
#        for dirs in dirlist:
#            full_dir_orig = os.path.join(orig_drive,dirs)
#            full_dir_dest = os.path.join(dest_drive,dirs)
#            if not os.path.exists(full_dir_orig):
#                print (full_dir_orig,'does not exist!')
#            else:
#                print (full_dir_orig)

#            if not os.path.exists(full_dir_dest):
#                print (full_dir_dest,'does not exist!')
#            else:
#                print (full_dir_dest)
    return(numfiles, folders)
    