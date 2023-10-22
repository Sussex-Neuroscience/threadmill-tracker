import numpy as np
from PIL import Image
import os
from matplotlib import pyplot as plt


dataFolder = "/home/andre/Downloads/channel2/"
files = os.listdir(dataFolder)




#im = Image.open(dataFolder+'00100.tif')
#imArray = np.array(im)#,dtype="int8")
#test = np.reshape(imArray,(1,-1))

#plt.plot(imArray)
#plt.show()

#plt.plot(test)
#plt.show()
#sessionData= np.zeros(1)

for index, item in enumerate(files):
    #load one image
    im = Image.open(dataFolder+item)
    #convert it to numpy array
    imArray = np.array(im)
    #reshape the 2D array into a column with several rows
    imArray = np.reshape(imArray,(-1,1))
    #if it is loading the first file in the folder, than store it under a new variable name
    if index == 0:
        sessionData = imArray
    #if not the first file in folder, start putting arrays together
    else:
        sessionData = np.concatenate((sessionData,imArray))

#normalize it
sessionData=sessionData/np.max(sessionData)
