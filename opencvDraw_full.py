import cv2
import numpy as np
import csv
import os

with open ('./pathToCsv.csv','r') as csvfile:
  fileReader = csv.reader(csvfile, delimiter=',')
  for row in fileReader:
    fileName = os.path.basename(row[0])
    print(fileName)
    if os.path.exists('./output/'+fileName):
      print("file is there: "+fileName)
      image = cv2.imread('output/'+fileName,0)
    else:
      image = cv2.imread(fileName,0)
    draw = image.copy()
    b1 = int(row[1])
    b2 = int(row[2])
    w  = int(row[3])
    h  = int(row[4])
    labels_to_names = {0: "dont_know", 1: "person", 2: "bicycle", 3: "car", 4: "motorcycle", 5: "airplane", 6: "bus", 7: "train", 8: "truck", 9: "boat", 10: "trafficlight", 11: "firehydrant", 12: "streetsign", 13: "stopsign", 14: "parkingmeter", 15: "bench", 16: "bird", 17: "cat", 18: "dog", 19: "horse", 20: "sheep", 21: "cow", 22: "elephant", 23: "bear", 24: "zebra", 25: "giraffe", 26: "hat", 27: "backpack", 28: "umbrella", 29: "shoe", 30: "eyeglasses", 31: "handbag", 32: "tie", 33: "suitcase", 34: "frisbee", 35: "skis", 36: "snowboard", 37: "sportsball", 38: "kite", 39: "baseballbat", 40: "baseballglove", 41: "skateboard", 42: "surfboard", 43: "tennisracket", 44: "bottle", 45: "plate", 46: "wineglass", 47: "cup", 48: "fork", 49: "knife", 50: "spoon", 51: "bowl", 52: "banana", 53: "apple", 54: "sandwich", 55: "orange", 56: "broccoli", 57: "carrot", 58: "hotdog", 59: "pizza", 60: "donut", 61: "cake", 62: "chair", 63: "couch", 64: "pottedplant", 65: "bed", 66: "mirror", 67: "diningtable", 68: "window", 69: "desk", 70: "toilet", 71: "door", 72: "tv", 73: "laptop", 74: "mouse", 75: "keyboard", 76: "cellphone", 77: "microwave", 78: "oven", 79: "toaster", 80: "sink", 81: "refrigerator", 82: "blender", 83: "book", 84: "clock", 85: "clock", 86: "vase", 87: "scissors", 88: "teddybear", 89: "hairdrier", 90: "toothbrush", 91: "hairbrush", 93: "small_cars"}
    row5 = int(row[5])
    print(row5)
    ln = labels_to_names[row5]
    print(ln)
    cv2.rectangle(draw, (b1,b2), (w,h), (0, 0, 255), 3)
    caption = "{}".format(ln)
    cv2.putText(draw, caption, (b1, b2 - 10), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), 2)
    cv2.imwrite('output/'+fileName,draw)
