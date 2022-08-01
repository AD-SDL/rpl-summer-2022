import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
data_growth = pd.read_excel('heatmap_data_pyhamilton.xlsx',engine='openpyxl')
c = np.array(data_growth)
data_nitrogen = pd.read_excel('nitrogen_heatmap.xlsx',engine='openpyxl')
a = np.array(data_nitrogen)
data_carbon = pd.read_excel('carbon_heatmap.xlsx',engine='openpyxl')
b = np.array(data_carbon)
data_phosphorus = pd.read_excel('phosphorus_heatmap.xlsx',engine='openpyxl')
d = np.array(data_phosphorus)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
img = ax.scatter(a, b, d, c=c, cmap=plt.hot())

ax.set_xlabel('Nitrogen')
ax.set_ylabel('Carbon')
ax.set_zlabel('Phosphorus')
#fig.colorbar(img,location='left')
cb = plt.colorbar(img ,ax = [ax], location = 'left')
plt.show()
##################
import seaborn as sns
for i in range(1,4):
    data_growth = pd.read_excel("heatmap_"+str(i)+'.xlsx',engine='openpyxl')
    c = np.array(data_growth)
    fig = plt.figure()
    ax = sns.heatmap(c , linewidth = 0.5 , cmap = 'coolwarm' )
    plt.title("Assay"+str(i))
    plt.savefig("Results_pyhamilton"+str(i))
