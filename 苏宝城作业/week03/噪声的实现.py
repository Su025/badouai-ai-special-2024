import numpy as np
import cv2 as cv
import random
#高斯噪声的实现
def GaussianNoise(src,means,sigma,percetage): #参数：图像、期望、sigma及百分比）
    Img=src
    Num=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX = random.randint(0, src.shape[0]-1) 
        randY = random.randint(0, src.shape[1]-1)
        Img[randX,randY] += random.gauss(means,sigma)
        #阈值处理
        if  Img[randX, randY]< 0:
            Img[randX, randY]=0
        elif Img[randX, randY]>255:
            Img[randX, randY]=255
    return Img

#椒盐噪声的实现
def  JiaoYanNoise(src,percetage):     
    Img=src    
    Num=int(percetage*src.shape[0]*src.shape[1])    
    for i in range(NoiseNum): 
	    randX = random.randint(0, src.shape[0]-1)       
	    randY = random.randint(0, src.shape[1]-1) 
	    
	    if random.random()<=0.5:           
	    	Img[randX,randY] = 0       
	    else:            
	    	Img[randX,randY] = 255    
    return Img

img = cv.imread('lenna.jpg')
noise_gs_img=util.random_noise(img,mode='poisson')
