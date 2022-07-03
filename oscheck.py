import os, sys, platform
from dataread import dataread

## ---Check the OS type and compatibility--- ##
def oscheck():
    if platform.system() == 'Windows':
        orig = 'D:\\'
        dest = 'E:\\'
        banner(platform.system(), orig, dest)
        dataread (orig, dest)
    elif platform.system() == 'Linux':
        orig = '/mnt/d/'
        dest = '/mnt/e/'
        banner(platform.system(), orig, dest)
        dataread (orig, dest)
    else:
        print (platform.system(),'NOT COMPATIBLE')

def banner(os, orig, dest):
    print('\n     ##############################################\n')
    print('         Detected Operating System: ',os)
    print('\n     ##############################################\n')
    print('         Source path:       ', orig)
    print('         Destination path:  ', dest)
    print('\n     ##############################################\n')