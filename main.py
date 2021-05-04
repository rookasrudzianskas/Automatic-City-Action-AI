import cv2

# Our image
img_file = 'Car_Detector.png'

classifier_file = 'cars.xml'

# open the image
img = cv2.imread(img_file)

# display the detected car image
cv2.imshow("Rokas Car Detector", img)

# Dont autoclous until the key is pressed
cv2.waitKey()














print("COMPLETED")