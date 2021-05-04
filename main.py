import cv2
from random import randint

# # Our image
# img_file = 'Car_Detector.png'
#
# classifier_file = 'cars.xml'
#
# # open the image
# img = cv2.imread(img_file)
#
#
# #  create a car classifier
#
# car_tracker = cv2.CascadeClassifier(classifier_file)
# # black and white image
# black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # detect cars
#
# cars = car_tracker.detectMultiScale(black_n_white)
#
# for (x, y, w, h) in cars:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (randint(0, 256), randint(0, 256), randint(0, 256)), 4)
#
# print(cars)
#
# # display the detected car image
# cv2.imshow("Rokas Car Detector", img)
#
# # Dont autoclous until the key is pressed
# cv2.waitKey()
#
#


# Our image
video_file = cv2.VideoCapture('Tesla Dash Cam Records Crazy Accident!.mp4')

classifier_file = 'cars.xml'

#  run forever
while True:
    # reads the current frame
    read_successful, frame = video_file.read()


#  create a car classifier

car_tracker = cv2.CascadeClassifier(classifier_file)
# black and white image
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect cars

cars = car_tracker.detectMultiScale(black_n_white)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randint(0, 256), randint(0, 256), randint(0, 256)), 4)

print(cars)

# display the detected car image
cv2.imshow("Rokas Car Detector", img)

# Dont autoclous until the key is pressed
cv2.waitKey()













print("COMPLETED")