import glob
import os

new_files = glob.glob('*.new')
for f in new_files:
    print('rm ' + f)
    os.system('rm ' + f)

print("Cleaned " + str(len(new_files)) + ' files.')

