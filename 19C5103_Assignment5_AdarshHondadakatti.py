import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("C:\Code From VScode\Python\Software Lab ASSIGNMENT\mango.jpg")
cv.imshow('Image',img)

# PutText
putText = cv.putText(img.copy(),"Two sliced mangoes",(10,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
cv.imshow('PutText Image',putText)

# Circle
circle = cv.circle(img.copy(),(300,300),100,(0,255,0),2)
cv.imshow('Circle',circle)

# Hstack
mango = cv.imread("C:\Code From VScode\Python\Software Lab ASSIGNMENT\mango.jpg")
guava = cv.imread("C:\Code From VScode\Python\Software Lab ASSIGNMENT\guava.jpg")
image1 = cv.resize(mango, (0, 0), None, .25, .25)
image2 = cv.resize(guava, (0, 0), None, .25, .25)
guava_mango = np.hstack(image1,image2)
cv.imshow('Hstack Image',guava_mango)

# Histogram
gray = cv.cvtColor(img.copy(),cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray],[0],gray,[256],[0,256])

plt.figure()
plt.title("Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Barplot
city = ['Bhopal','Indore','Ujjain','Rewa','Dewas']
temp = [37,35,39,33,32]

plt.bar(city,temp,color='blue')
plt.ylabel('Temperature')
plt.ylabel('City')
plt.title("Temperature of cities of MP")
plt.show()

cv.waitKey(0)
