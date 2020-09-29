from netCDF4 import Dataset
import matplotlib.pyplot as plt
from wrf import to_np, getvar, get_basemap, latlon_coords
import sys
import numpy as np
import landuse_colormap as lu_cm
geo_em_file = Dataset(sys.argv[1])
lis_input_file = Dataset(sys.argv[2])

var = getvar(geo_em_file, 'LU_INDEX', timeidx=0)

lats, lons = latlon_coords(var)
bm = get_basemap(var, resolution='h')
x, y = bm(to_np(lons), to_np(lats))

lu_index = lis_input_file['LANDCOVER'][:]
lu_index_proc = lu_index * np.reshape(np.arange(1,len(lu_index) + 1, 1), (len(lu_index), 1, 1))
lu_index_proc = np.sum(lu_index_proc, axis=0)

# Get land cover schemes
scheme = lis_input_file.LANDCOVER_SCHEME

if scheme == 'IGBPNCEP':
    cm, labels = lu_cm.LU_MODIS21()
elif scheme == 'USGS':
    cm, labels = lu_cm.LU_USGS24()
elif scheme == 'UMD':
    cm, labels = lu_cm.LU_UMD()
else:
    print("Invalid scheme: " + scheme)
    sys.exit()

plt.figure(figsize=(12,9))
try:
    bm.drawcoastlines()
except:
    print("Unable to draw coastlines")
bm.drawstates()
bm.drawcountries()

plt.pcolormesh(x, y, lu_index_proc, cmap=cm, vmin=0.5, vmax=len(labels)+0.5)
cbar = plt.colorbar(shrink=1)
cbar.set_ticks(np.arange(1,len(labels)+1,1))
cbar.ax.set_yticklabels(labels)
cbar.ax.invert_yaxis()
cbar.ax.tick_params(labelsize=12)

plt.tight_layout()
plt.show()

