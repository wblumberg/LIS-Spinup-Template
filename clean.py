import glob
import os

new_files = glob.glob('*.new')
for f in new_files:
    print('rm ' + f)
    os.system('rm ' + f)

print("Cleaned " + str(len(new_files)) + ' files.')

tbl = glob.glob("*.TBL")
for t in tbl:
    print('rm ' + t)
    os.system('rm ' + t)

print("Cleaned " + str(len(tbl)) + ' files.')

print("Cleaning LDT/LIS config files.")
for t in ['ldt.config.postlis', 'ldt.config.prelis', 'lis.config.coldstart', 'lis.config.wrf']:
    os.system('rm ' + t)
    os.system('rm ' + t + '.new')

