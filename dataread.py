from countfiles import countfiles
import os
def dataread (orig, dest):
    abs_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
#    print (abs_file_path)
    pathlist = open(abs_file_path, 'r')
    tot_f_orig = 0
    tot_f_dest = 0
    while True:
        line = pathlist.readline()
        if not line:
            break
        a = countfiles(orig+line.strip())
        b = countfiles(dest+line.strip())
        if a[0] == b[0]:
            print('     Same number of files detected for:', line.strip())
        else:
            print('     ##############################################')
            print('     ', a[0], 'files in', a[1])        
            print('     ', b[0], 'files in', b[1])
            print('     ##############################################')
        tot_f_orig += int(a[0])
        tot_f_dest += int(b[0])
    print('\n     #################################################')    
    print('     ##                                             ##')
    print('     ##  Total files found in origin:      ',tot_f_orig,'  ##')
    print('     ##  Total files found in destination: ',tot_f_dest,'  ##')
    print('     ##                                             ##')
    print('     #################################################\n')
    pathlist.close()