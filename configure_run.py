import glob
import sys
import os

# Check for geo_em and namelist.wps

namelist = glob.glob('namelist.wps')
geo_em = glob.glob('geo_em*.nc')

if len(namelist) == 0:
    print("Missing namelist.wps")
    sys.exit()

if len(geo_em) == 0:
    print("Missing geo_ems from WPS")
    sys.exit()

# get all of the .reg files and update the DIR
cur_dir = os.getcwd()
regs = glob.glob('*.reg')
for r in regs:
    f = open(r, 'r')
    contents = f.read()
    contents = contents.replace('%DIR%', cur_dir)
    f2 = open(r + '.new', 'w')
    f2.write(contents)
    f2.close()
    f.close()

