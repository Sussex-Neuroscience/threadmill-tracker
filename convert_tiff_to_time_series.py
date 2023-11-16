import numpy as np
from PIL import Image
import os
#from matplotlib import pyplot as plt
from scipy.io import savemat


#users will need to change the following line to point to the location where their data is
dataFolder = "C:\\Users\\Andre Maia Chagas\\Box\\Locomotion data (convert images to time series)\\channel2\\"
#get all files in the folder
files = os.listdir(dataFolder)
#sort the files list in ascending order
files = sorted(files)

# tiffs = 0
# for index, item in enumerate(files):
#     #make sure we are only using the tif files inside the folder
#     if item[-3:]=="tif":
#         tiffs=tiffs+1
#         
#         print ("preprocessing file:" + str(item))    
#         #load one stack
#         im = Image.open(dataFolder+item)
#         #get the number of frames in the stack
#         if index == 0:
#             nFrames = im.n_frames
#             #get the shape of the frame
#             h,w = np.shape(im)
#         else:
#             if im.n_frames>nFrames:
#                 nFrames=im.n_frames
#                 print("max frames:" +str(nFrames))



        
#allData=dict()
trialNum = 0
for index, item in enumerate(files):
    #make sure we are only using the tif files inside the folder
    if item[-3:]=="tif":
        trialNum=trialNum+1
        print ("processing file:" + str(item))    
        #load one stack
        im = Image.open(dataFolder+item)
        #get the number of frames in the stack
        nFrames = im.n_frames
        #get the shape of the frame
        h,w = np.shape(im)
        #tiffarray = np.zeros((h,w,nFrames))
        trialData=np.zeros(h*w*nFrames)-50
        for i in range(nFrames):
            im.seek(i)
            imArray = np.array(im)
            #tiffarray[:,:,i] = np.array(im)
            #reshape each frame into a column with several rows
            imArray = np.reshape(imArray,(-1,1))
            
            
            #if it is loading the first file in the folder, than store it under a new variable name
            #allFrames[0:,i,tiffs]=imArray.flatten()
            trialData[i*h*w:(i*h*w)+(h*w)]=imArray.flatten()
            #print(str(i*h*w)+" to "+str((i*h*w)+(h*w)))
            #if index == 0:
            #    trialData = imArray
            #if not the first file in folder, start putting arrays together
            #else:                
            #    trialData = np.concatenate((trialData,imArray))
        
        #normalize trialData
        #print("trial "+str(trialNum))
        #print(str(np.min(trialData)))
        #print(str(np.max(trialData)))
        #trialDataNorm=trialData/np.max(trialData)
        
        #allData["trial "+str(trialNum)]=trialData.astype(np.int64)
        #prepare data for saving as .mat
#         
        mdic={item: trialData,'label': 'raw'}
        savemat(dataFolder+item[0:-4]+".mat",mdic)
#         #tiffs=tiffs+1
#         
# #         for i in range(tiffarray.shape[2]):
# #             frame = 
# #             #reshape each frame into a column with several rows
# #             imArray = np.reshape(tiffarray,(-1,1,frame))
# #             #if it is loading the first file in the folder, than store it under a new variable name
# #             if index == 0:
# #                 sessionData = imArray
# #             #if not the first file in folder, start putting arrays together
# #             else:
# #                 sessionData = np.concatenate((sessionData,imArray))
# 
# #normalize it
# #alltrials=alltrials/np.max(alltrials)
# 
#prepare data for saving as .mat
#mdic={'threadmill': allData,'label': 'raw'}
# 
#save data as .mat
#savemat(dataFolder+"threadmill.mat",mdic)
# 
# 
# #im = Image.open(dataFolder+'00100.tif')
# #imArray = np.array(im)#,dtype="int8")
# #test = np.reshape(imArray,(1,-1)) 	
# 
# #plt.plot(imArray)
# #plt.show()
# 
# #plt.plot(test)
# #plt.show()
# #sessionData= np.zeros(1)