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


