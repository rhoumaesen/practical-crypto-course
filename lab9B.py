from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

randomimg = np.random.randint(255, size=(200,200,3),dtype=np.uint8)
plt.imshow(randomimg)
plt.subplot(221), plt.imshow(randomimg )
plt.subplot(222), plt.hist(randomimg[:,:,0].ravel(),256,[0,256],color = "red"); 
plt.subplot(223), plt.hist(randomimg[:,:,1].ravel(),256,[0,256],color = "green"); 
plt.subplot(224), plt.hist(randomimg[:,:,2].ravel(),256,[0,256],color = "blue"); 
plt.show()
