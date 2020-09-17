import glob
import sys
import os
from datetime import datetime

def get_forcing_list_file(force_type):
    if force_type == 'NLDAS2':
        return "./forcing_variables_nldas2.txt"  
    elif force_type == 'GDAS':
        return './forcing_variables_gdas.txt'
    elif force_type == 'MERRA-Land':
        return './forcing_variables_merraland.txt'
    elif force_type == 'MERRA2':
        return './forcing_variables_merra2.txt'
    else:
        print("NOT A VALID FORCING")
        return ""

def get_landuse_settings(lu_type):
    f = open('landuse/' + lu_type.lower(), 'r')
    settings = f.read()
    f.close()
    return settings

def get_model_output_attr_files(lsm):
    coldstart = ""
    wrf = ""
    if lsm == 'Noah.3.6':
        return "NOAH36_OUTPUT_LIST_SPINUP.TBL", "NOAH36_OUTPUT_LIST.TBL"
    elif lsm == 'Noah MP 3.6':
        return "NOAHMP_OUTPUT_LIST_SPINUP.TBL", "NOAHMP_OUTPUT_LIST.TBL"
    elif lsm == 'Noah.3.3':
        return "NOAH33_OUTPUT_LIST_SPINUP.TBL", "NOAH33_OUTPUT_LIST.TBL"
    else:
        print("NOT A VALID LSM")
        return ""

def sdt2file(sdt, prefix, file_string):
    dt = datetime.strptime(sdt, "%Y-%m-%d %H:%M:%S")
    for dt_fmt, time_unit in zip(['%Y', '%m', '%d', '%H', '%M', '%S'], ['YEAR', 'MONTH', 'DAY', 'HOUR', 'MIN', 'SEC']):
        field = '*' + prefix + time_unit + '*'
        file_string = file_string.replace(field, dt_fmt)
    file_string = dt.strftime(file_string)
    return file_string


##########################################################################
#
#   Core variables for code.
#
forcing_options = ['MERRA2', 'MERRA-Land', 'GDAS', "NLDAS2"]
lsm_options = ["noah36", "noahmp36", "noah33"]
lu_options = ['USGS', "UMD", "MODIS"]

lsm = "Noah.3.6" # ONLY Noah.3.6 supported right now
landuse = 'MODIS'
forcing = "NLDAS2"
lis_start_sdt = '2012-05-01 00:00:00'
lis_end_sdt = '2013-05-01 00:00:00'
lis_out_sdt = '2013-04-30 12:00:00'
wrf_start_sdt = '2013-05-01 00:00:00'
wrf_end_sdt = '2013-05-02 00:00:00'
wrf_time_step = '18ss'
npx = 8
npy = 14
wrf_dir = '/discover/nobackup/wgblumbe/test_lis_deployment/' # NEEDS TO BE AN ABSOLUTE PATH - THIS IS THE DIRECTORY THE WRF RUN IS IN
##########################################################################

# Check for geo_em and namelist.wps
namelist = glob.glob(wrf_dir + 'namelist.wps')
geo_em = glob.glob(wrf_dir + 'geo_em*.nc')
real_namelist = glob.glob(wrf_dir + 'namelist.input.real')
wrf_namelist = glob.glob(wrf_dir + 'namelist.input.wrf')

if len(namelist) == 0:
    print("Missing namelist.wps")
    sys.exit()

if len(geo_em) == 0:
    print("Missing geo_ems from WPS")
    sys.exit()

###########################
#
# Starting main code block
#
###########################

coldstart_attr, wrf_attr = get_model_output_attr_files(lsm)
forcing_files = get_forcing_list_file(forcing)

#------------------------------------
### UPDATING THE .REG FILES
#------------------------------------
print("Updating the *.reg files to have the correct run directory")
cur_dir = wrf_dir
regs = glob.glob('*.reg')
for r in regs:
    f = open(r, 'r')
    contents = f.read()
    contents = contents.replace('%DIR%', cur_dir)
    f2 = open(r + '.new', 'w')
    f2.write(contents)
    f2.close()
    f.close()

print("Making sure the ntasks for lis.reg matches those in the config file")
lis_reg_f = open('lis.reg.new', 'r')
lis_reg = lis_reg_f.read()
lis_reg_f.close()
lis_reg = lis_reg.replace('*NTASKS*', str(npx*npy))

# lis.reg needs to copy the correct restart and history files
lis_end_dt = datetime.strptime(lis_end_sdt, '%Y-%m-%d %H:%M:%S')
lis_reg = lis_end_dt.strftime(lis_reg)

lis_reg_f = open('lis.reg.new', 'w')
lis_reg_f.write(lis_reg)
lis_reg_f.close()

#------------------------------------
### SETUP THE LDT.CONFIG.PRELIS FILE
#------------------------------------
print("Setting up the ldt.config.prelis file...")
ldt_prelis_file = open('ldt.config.prelis.template', 'r')
ldt_prelis = ldt_prelis_file.read()
ldt_prelis_file.close()

# Update LSM field
ldt_prelis = ldt_prelis.replace('*LSMMODEL*', lsm)
# Update number of nests
ldt_prelis = ldt_prelis.replace('*NUMNESTS*', str(1))

# Append land cover settings to file
lc_settings = get_landuse_settings(landuse)
ldt_prelis = ldt_prelis + '\n' + lc_settings

#------------------------------------
### SETUP THE LDT.CONFIG.POSTLIS FILE
#------------------------------------
print("Setting up the ldt.config.postlis file...")
ldt_postlis_file = open('ldt.config.postlis.template', 'r')
ldt_postlis = ldt_postlis_file.read()
ldt_postlis_file.close()

# Update LSM field
ldt_postlis = ldt_postlis.replace('*LSMMODEL*', lsm)
# Update number of nests
ldt_postlis = ldt_postlis.replace('*NUMNESTS*', str(1))

# Append land cover settings to file
lc_settings = get_landuse_settings(landuse)
ldt_postlis = ldt_postlis + '\n' + lc_settings

# Add history files
hist_file_fmt = './LIS_HIST_%Y%m%d%H%M.d01.nc'
lis_end_dt = datetime.strptime(lis_end_sdt, '%Y-%m-%d %H:%M:%S')
lis_hist_file = lis_end_dt.strftime(hist_file_fmt)
ldt_postlis = ldt_postlis.replace('*LISHIST1*', lis_hist_file)

#---------------------------------------
### SETUP THE LIS.CONFIG.COLDSTART FILE
#---------------------------------------
print("Setting up the lis.config.coldstart file...")
lis_coldstart_f = open('lis.config.coldstart.template', 'r')
lis_coldstart = lis_coldstart_f.read()
lis_coldstart_f.close()

# Add forcing datasets to the file
forcing_settings_f = open('forcings.txt', 'r')
forcing_settings = forcing_settings_f.read()
forcing_settings_f.close()
lis_coldstart = lis_coldstart + '\n' + forcing_settings

# Add LSM parameters
parameters_settings_f = open('parameters.txt', 'r')
parameters_settings = parameters_settings_f.read()
parameters_settings_f.close()
lis_coldstart = lis_coldstart + '\n' + parameters_settings

# update LSM field
lis_coldstart = lis_coldstart.replace('*LSMMODEL*', lsm)
# Update number of nests
lis_coldstart = lis_coldstart.replace('*NUMNESTS*', str(1))
# Update met forcing field
lis_coldstart = lis_coldstart.replace('*METFORCING*', "\"" + forcing + "\"")
# Update processor numbers
lis_coldstart = lis_coldstart.replace('*NPY*', str(npy))
lis_coldstart = lis_coldstart.replace('*NPX*', str(npx))
# Input start/end times for LIS run
lis_coldstart = sdt2file(lis_start_sdt, 'START', lis_coldstart)
lis_coldstart = sdt2file(lis_end_sdt, 'END', lis_coldstart)
# Add in the forcing list file
lis_coldstart = lis_coldstart.replace('*FORCINGVARSFILE*', forcing_files)
# Spinup output start date
lis_coldstart = sdt2file(lis_out_sdt, 'OUT', lis_coldstart)
# Model output attributes file
lis_coldstart = lis_coldstart.replace('*MODELOUTPUTFILETBL*', coldstart_attr) 

#---------------------------------------
### SETUP THE LIS.CONFIG.WRF FILE
#---------------------------------------
print("Setting up the lis.config.wrf file...")
lis_wrf_f = open('lis.config.wrf.template', 'r')
lis_wrf = lis_wrf_f.read()
lis_wrf_f.close()

# Add forcing datasets to the file
forcing_settings_f = open('forcings.txt', 'r')
forcing_settings = forcing_settings_f.read()
forcing_settings_f.close()
lis_wrf = lis_wrf + '\n' + forcing_settings

# Add LSM parameters
parameters_settings_f = open('parameters.txt', 'r')
parameters_settings = parameters_settings_f.read()
parameters_settings_f.close()
lis_wrf = lis_wrf + '\n' + parameters_settings

# update LSM field
lis_wrf = lis_wrf.replace('*LSMMODEL*', lsm)
# Update number of nests
lis_wrf = lis_wrf.replace('*NUMNESTS*', str(1))
# Update met forcing field
lis_wrf = lis_wrf.replace('*METFORCING*', "\"" + forcing + "\"")
# Update processor numbers
lis_wrf = lis_wrf.replace('*NPY*', str(npy))
lis_wrf = lis_wrf.replace('*NPX*', str(npx))
# Input start/end times for LIS run
lis_wrf = sdt2file(wrf_start_sdt, 'WRFSTART', lis_wrf)
lis_wrf = sdt2file(wrf_end_sdt, 'WRFEND', lis_wrf)
# Model output attributes file
lis_wrf = lis_wrf.replace('*MODELOUTPUTFILETBL*', wrf_attr) 
# Restart file
restart_file_fmt = './LIS_RST_NOAH36_%Y%m%d%H%M.d01.nc'
lis_end_dt = datetime.strptime(lis_end_sdt, '%Y-%m-%d %H:%M:%S')
lis_restart_file = lis_end_dt.strftime(restart_file_fmt)
lis_wrf = lis_wrf.replace('*RSTFILED1*', lis_restart_file)
# Add in WRF time step for LSM timestep
lis_wrf = lis_wrf.replace('*D1DS*', wrf_time_step)

print("\nCompleted setting up ldt.config and lis.config files.")

#---------------------------------------
### RUN lisWrfDomain.py
#---------------------------------------
f = open('lis.config.wrf', 'w')
f.write(lis_wrf)
f.close()

f = open('lis.config.coldstart', 'w')
f.write(lis_coldstart)
f.close()

f = open('ldt.config.postlis', 'w')
f.write(ldt_postlis)
f.close()

f = open('ldt.config.prelis', 'w')
f.write(ldt_prelis)
f.close()

os.system('./lisWrfDomain.py EXE lis.config.coldstart ldt.config.prelis ' + wrf_dir)
os.system('./lisWrfDomain.py EXE lis.config.wrf ldt.config.postlis ' + wrf_dir)

#---------------------------------------
### COPY OVER FILES TO RUN DIR
#---------------------------------------

print("Copying built files to " + wrf_dir)
all_new_files = glob.glob('*.new')
for f in all_new_files:
    print('Copying ' + f)
    os.system('cp ' + f + ' ' + wrf_dir + '/' + f.replace('.new', ''))

for f in ['output_lists/' + coldstart_attr, 'output_lists/' + wrf_attr, 'forcing_variables/' + forcing_files, 'forcing_variables/forcing_variables_wrfcplmode.txt']:
    print("Copying " + f)
    os.system('cp ' + f + ' ' + wrf_dir + '/')

