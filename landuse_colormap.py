## Custom Terrain ColorMaps by Brian

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Four Different Land Use Categories:
#   LU_MODIS20
#   LU_MODIS21     includes lake category
#   LU_USGS24
#   LU_NLCD
#   LU_UMD
#   LU_MOD12C1

## Land Use Colormap
## ! represents categories not in my Utah domain
def LU_MODIS21(): #
    C = np.array([
    [0,.4,0],      #  1 Evergreen Needleleaf Forest
    [0,.4,.2],      #! 2 Evergreen Broadleaf Forest    
    [.2,.8,.2],     #  3 Deciduous Needleleaf Forest
    [.2,.8,.4],     #  4 Deciduous Broadleaf Forest
    [.2,.6,.2],     #  5 Mixed Forests
    [.3,.7,0],      #  6 Closed Shrublands
    [.82,.41,.12],     #  7 Open Shurblands
    [.74,.71,.41],       #  8 Woody Savannas
    [1,.84,.0],     #  9 Savannas
    [0,1,0],        #  10 Grasslands
    [0,1,1],        #! 11 Permanant Wetlands
    [1,1,0],      #  12 Croplands
    [1,0,0],     #  13 Urban and Built-up
    [.7,.9,.3],      #! 14 Cropland/Natual Vegation Mosaic
    [1,1,1],        #! 15 Snow and Ice
    [.914,.914,.7], #  16 Barren or Sparsely Vegetated
    [.5,.7,1],        #  17 Water (like oceans)
    [.86,.08,.23],        #  18 Wooded Tundra
    [.97,.5,.31],        #! 19 Mixed Tundra
    [.91,.59,.48],     #! 20 Barren Tundra
    [0,0,.88]])      #! 21 Lake
    
   
    cm = ListedColormap(C)
    
    labels = ['Evergreen Needleleaf Forest',
              'Evergreen Broadleaf Forest',
              'Deciduous Needleleaf Forest',
              'Deciduous Broadleaf Forest',
              'Mixed Forests',
              'Closed Shrublands',
              'Open Shrublands',
              'Woody Savannas',
              'Savannas',
              'Grasslands',
              'Permanent Wetlands',
              'Croplands',
              'Urban and Built-Up',
              'Cropland/Natural Vegetation Mosaic',
              'Snow and Ice',
              'Barren or Sparsely Vegetated',
              'Water',
              'Wooded Tundra',
              'Mixed Tundra',
              'Barren Tundra',
              'Lake']    
    
    return cm, labels

def LU_MOD12C1(): #
    C = np.array([
    [0,0,.88],        #  0 Water
    [0,.4,0],         #  1 Evergreen Needleleaf Forest
    [0,.4,.2],        #! 2 Evergreen Broadleaf Forest    
    [.2,.8,.2],       #  3 Deciduous Needleleaf Forest
    [.2,.8,.4],       #  4 Deciduous Broadleaf Forest
    [.2,.6,.2],       #  5 Mixed Forests
    [.3,.7,0],        #  6 Closed Shrublands
    [.82,.41,.12],    #  7 Open Shurblands
    [.74,.71,.41],    #  8 Woody Savannas
    [1,.84,.0],       #  9 Savannas
    [0,1,0],          #  10 Grasslands
    [0,1,1],          #! 11 Permanant Wetlands
    [1,1,0],          #  12 Croplands
    [1,0,0],          #  13 Urban and Built-up
    [.7,.9,.3],       #! 14 Cropland/Natual Vegation Mosaic
    [1,1,1],          #! 15 Snow and Ice
    [.914,.914,.7]])   #  16 Barren or Sparsely Vegetated

    cm = ListedColormap(C)
    
    labels = ['Water',
              'Evergreen Needleleaf Forest',
              'Evergreen Broadleaf Forest',
              'Deciduous Needleleaf Forest',
              'Deciduous Broadleaf Forest',
              'Mixed Forests',
              'Closed Shrublands',
              'Open Shrublands',
              'Woody Savannas',
              'Savannas',
              'Grasslands',
              'Permanent Wetlands',
              'Croplands',
              'Urban and Built-Up',
              'Cropland/Natural Vegetation Mosaic',
              'Snow and Ice',
              'Barren or Sparsely Vegetated']
    
    return cm, labels

def LU_MODIS20(): #
    C = np.array([
    [0,.4,0],         #  1 Evergreen Needleleaf Forest
    [0,.4,.2],        #! 2 Evergreen Broadleaf Forest    
    [.2,.8,.2],       #  3 Deciduous Needleleaf Forest
    [.2,.8,.4],       #  4 Deciduous Broadleaf Forest
    [.2,.6,.2],       #  5 Mixed Forests
    [.3,.7,0],        #  6 Closed Shrublands
    [.82,.41,.12],    #  7 Open Shurblands
    [.74,.71,.41],    #  8 Woody Savannas
    [1,.84,.0],       #  9 Savannas
    [0,1,0],          #  10 Grasslands
    [0,1,1],          #! 11 Permanant Wetlands
    [1,1,0],          #  12 Croplands
    [1,0,0],          #  13 Urban and Built-up
    [.7,.9,.3],       #! 14 Cropland/Natual Vegation Mosaic
    [1,1,1],          #! 15 Snow and Ice
    [.914,.914,.7],   #  16 Barren or Sparsely Vegetated
    [0,0,.88],        #  17 Water
    [.86,.08,.23],    #  18 Wooded Tundra
    [.97,.5,.31],     #! 19 Mixed Tundra
    [.91,.59,.48]])   #! 20 Barren Tundra

    cm = ListedColormap(C)
    
    labels = ['Evergreen Needleleaf Forest',
              'Evergreen Broadleaf Forest',
              'Deciduous Needleleaf Forest',
              'Deciduous Broadleaf Forest',
              'Mixed Forests',
              'Closed Shrublands',
              'Open Shrublands',
              'Woody Savannas',
              'Savannas',
              'Grasslands',
              'Permanent Wetlands',
              'Croplands',
              'Urban and Built-Up',
              'Cropland/Natural Vegetation Mosaic',
              'Snow and Ice',
              'Barren or Sparsely Vegetated',
              'Water',
              'Wooded Tundra',
              'Mixed Tundra',
              'Barren Tundra']
    
    return cm, labels
 
def LU_USGS24():
    
    C = np.array([
    [1,0,0],          #  1 Urban and Built-up Land
    [1,1,0],          #! 2 Dryland Cropland and Pasture
    [1,1,.2],         #  3 Irrigated Cropland and Pasture
    [1,1,.3],         #  4 Mixed Dryland/Irrigated Cropland and Pasture
    [.7,.9,.3],       #  5 Cropland/Grassland Mosaic
    [.7,.9,.3],       #  6 Cropland/Woodland Mosaic
    [0,1,0],          #  7 Grassland
    [.3,.7,0],        #  8 Shrubland
    [.82,.41,.12],    #  9 Mixed Shrubland/Grassland
    [1,.84,.0],       #  10 Savanna
    [.2,.8,.4],       #  11 Deciduous Broadleaf Forest
    [.2,.8,.2],       #  12 Deciduous Needleleaf Forest
    [0,.4,.2],        #  13 Evergreen Broadleaf Forest
    [0,.4,0],         #! 14 Evergreen Needleleaf Forest 
    [.2,.6,.2],       #  15 Mixed Forests
    [0,0,.88],        #  16 Water Bodies
    [0,1,1],          #! 17 Herbaceous Wetlands
    [.2,1,1],         #  18 Wooden Wetlands
    [.914,.914,.7],   #  19 Barren or Sparsely Vegetated
    [.86,.08,.23],    #  20 Herbaceous Tundraa
    [.86,.08,.23],    #  21 Wooded Tundra
    [.97,.5,.31],     #! 22 Mixed Tundra
    [.91,.59,.48],   #! 23 Barren Tundra
    [1,1,1]          #! 24 Snow and Ice
    ])
    
    cm = ListedColormap(C)
    
    labels = ['Urban and Built-up Land',
              'Dryland Cropland and Pasture',
              'Irrigated Cropland and Pasture',
              'Mixed Dryland/Irrigated Cropland and Pasture',
              'Cropland/Grassland Mosaic',
              'Cropland/Woodland Mosaic',
              'Grassland',
              'Shrubland',
              'Mixed Shrubland/Grassland',
              'Savanna',
              'Deciduous Broadleaf Forest',
              'Deciduous Needleleaf Forest',
              'Evergreen Broadleaf',
              'Evergreen Needleleaf',
              'Mixed Forest',
              'Water Bodies',
              'Herbaceous Wetland',
              'Wooden Wetland',
              'Barren or Sparsely Vegetated',
              'Herbaceous Tundra',
              'Wooded Tundra',
              'Mixed Tundra',
              'Bare Ground Tundra',
              'Snow or Ice']
    
    return cm, labels   
    
def LU_USGS_chris():
    # Provided by Chris Foster
    C = np.array([
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 1.0],
    [0.4, 0.4, 0.4],
    [0.0, 0.4, 0.2],
    [0.2, 0.6, 0.2],
    [0.3, 0.7, 0.0],
    [0.8, 1.0, 0.2],
    [0.0, 1.0, 0.0],
    [0.8, 0.4, 0.2],
    [0.6, 0.4, 0.0],  
    [1.0, 1.0, 1.0]   
    ])
    
    cm = ListedColormap(C)
    
    labels = ['Water',   
    'Wetland',
    'Devloped Urban',     
    'Evergreen Forest', 
    'Deciduous Forest',    
    'Irrigated Cropland and Pasture', 
    'Cropland/Grassland Mosaic', 
    'Grassland', 
    'Shrubland', 
    'Barren Land', 
    'High Albedo Surface'
    ]
    
    return cm, labels
    
def LU_NLCD_chris():
    # Provided by Chris Foster
    C = np.array([
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 1.0],
    [0.3, 0.3, 0.3],
    [0.4, 0.4, 0.4],
    [0.5, 0.5, 0.5],
    [0.6, 0.6, 0.6],
    [0.0, 0.4, 0.2],
    [0.2, 0.6, 0.2],
    [0.3, 0.7, 0.0],
    [0.8, 1.0, 0.2],
    [0.0, 1.0, 0.0],
    [0.8, 0.4, 0.2],
    [0.6, 0.4, 0.0]
    ])
    
    cm = ListedColormap(C)
    
    labels = ['Water', # 11
    'Wetland', # 90/95
    'Developed High Intensity', # 24
    'Developed Medium Intensity', #23
    'Developed Low Intensity', # 22
    'Developed Open Space', # 21
    'Evergreen Forest', # 42
    'Deciduous Forest', # 41
    'Cultivated Crops', # 82
    'Pasture/Hay', # 81 
    'Grassland', # 71
    'Shrubland', # 52/51
    'Barren Land' # 31
    ]
    
    return cm, labels

def LU_UMD():
    C = np.array([
    [0,.4,0],      #  1 Evergreen Needleleaf Forest
    [0,.4,.2],      #! 2 Evergreen Broadleaf Forest    
    [.2,.8,.2],     #  3 Deciduous Needleleaf Forest
    [.2,.8,.4],     #  4 Deciduous Broadleaf Forest
    [.2,.6,.2],     #  5 Mixed Forests
    [.3,.7,0],      #  6 Closed Shrublands
    [.82,.41,.12],     #  7 Open Shurblands
    [.74,.71,.41],       #  8 Woody Savannas
    [1,.84,.0],     #  9 Savannas
    [0,1,0],        #  10 Grasslands
    [1,1,0],      #  12 Croplands
    [1,0,0],     #  13 Urban and Built-up
    [.914,.914,.7], #  16 Barren or Sparsely Vegetated
    [.5,.7,1]])      #! 21 Lake
    
   
    cm = ListedColormap(C)
    
    labels = ['Evergreen Needleleaf Forest',
              'Evergreen Broadleaf Forest',
              'Deciduous Needleleaf Forest',
              'Deciduous Broadleaf Forest',
              'Mixed Forests',
              'Closed Shrublands',
              'Open Shrublands',
              'Woody Savannas',
              'Savannas',
              'Grasslands',
              'Croplands',
              'Urban and Built-Up',
              'Barren or Sparsely Vegetated',
              'Water']    
    
    return cm, labels

def LU_NLCD():
    C = np.array([
    [0.34, 0.46, 0.65], # Open water - 11
    [1.00, 1.00, 1.00], # Perennia ice/snow - 12
    [0.91, 0.82, 0.82], # Developed Open Space - 21
    [0.88, 0.62, 0.56], # Developed, low intensity - 22
    [0.98, 0.02, 0.11], # Developed, medium intensity - 23
    [0.70, 0.01, 0.06], # Developed, high intensity - 24
    [0.82, 0.80, 0.76], # Barren land (rock/sand/clay) - 31
    [0.53, 0.78, 0.52], # Deciduous Forest - 41
    [0.24, 0.51, 0.32], # Evergreen Forest - 42
    [0.83, 0.91, 0.71], # Mixed Forest - 43
    [0.68, 0.59, 0.28], # Dwarf Scrub - 51
    [0.86, 0.79, 0.58], # Shrub/Shrub - 52
    [0.99, 0.91, 0.69], # Grassland/Herbaceous - 71  
    [0.82, 0.82, 0.54], # Sedge/Herbaceous - 72
    [0.64, 0.80, 0.37], # Lichens - 73
    [0.52, 0.73, 0.62], # Moss - 74
    [0.98, 0.96, 0.44], # Pasture/Hay - 81
    [0.78, 0.57, 0.31], # Cultivated Crops - 82
    [0.79, 0.90, 0.97], # Woody Wetlands - 90
    [0.41, 0.70, 0.83], # Emerent Herbaceous Wetlands - 95
    ])
    
    cm = ListedColormap(C)
    
    labels = ['Open water',
    'Perennia ice/snow',
    'Developed Open Space', 
    'Developed Low Intensity', 
    'Developed Medium Intensity',  
    'Developed High Intensity', 
    'Barren Land',
    'Deciduous Forest', 
    'Evergreen Forest', 
    'Mixed Forest',
    'Dwarf Scrub',
    'Shrub/Shrub',
    'Grassland/Herbaceous',
    'Sedge/Herbaceous',
    'Lichens',
    'Moss',
    'Pasture/Hay', 
    'Cultivated Crops', 
    'Woody Wetlands',
    'Emergent Herbaceous Wetlands'
    ]
    
    return cm, labels

if __name__ == "__main__":
    # Grab colormap and labels    
    cm,labels = LU_MODIS21()
    
    #create some Land Use category field
    LU_INDEX = np.random.randint(0,len(labels)+1,(20,20))
    
    plt.figure(1)
    plt.title('Land Use Categories')
    plt.pcolormesh(LU_INDEX,cmap = cm,vmin=1,vmax=len(labels)+1) # for example. !!!MUST SET VMAX AND VMIN LIKE THIS TO SCALE COLOR RANGE CORRECTLY!!!
    cbar = plt.colorbar(shrink=1)
    cbar.set_ticks(np.arange(0.5,len(labels)+1))
    cbar.ax.set_yticklabels(labels)
    #cbar.ax.set_xticklabels(labels) #If using a horizontal colorbar orientation
    cbar.ax.invert_yaxis()
    
    cbar.ax.tick_params(labelsize=10)
    plt.show()

