from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

im = Image.open('nebula.png')
im_matrix = np.array(im)
print(im_matrix.shape)

#print(im_matrix[:,:,1])
#im = np.asarray(Image.open("nebula.png"))
#print(im.dtype )           
#print(im)

print(im_matrix[100,150])

plt.subplot(221), plt.imshow(im_matrix )
plt.subplot(222), plt.hist(im_matrix[:,:,0].ravel(),256,[0,256],color = "red"); 
plt.subplot(223), plt.hist(im_matrix[:,:,1].ravel(),256,[0,256],color = "green"); 
plt.subplot(224), plt.hist(im_matrix[:,:,2].ravel(),256,[0,256],color = "blue"); 

plt.show()

