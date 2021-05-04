import cv2

# Our image
img_file = 'Car_Detector.png'

classifier_file = 'cars.xml'

# open the image
img = cv2.imread(img_file)


#  create a car classifier

car_tracker = cv2.CascadeClassifier(classifier_file)
# black and white image
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




# display the detected car image
cv2.imshow("Rokas Car Detector", black_n_white)

# Dont autoclous until the key is pressed
cv2.waitKey()














print("COMPLETED")