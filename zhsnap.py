"""
ZHSnap - take photos and automatically create PDF and ZIP files in working directory
         (or just save the jpgs). Default filename (without suffix): zh_NEPTUNCODE, 
         jpg files are numbered in ascending order.
---
Packages installed (with pip): opencv-python, fpdf
---
Instructions:
  1) modify FILENAME variable accordingly
  2) start server in IP Webcam (if you want to use it, WEBCAM_PATH can be modified 
                                to 0 to use primary system camera)
                                [suggested setting: video preferences -> orientation: portrait]
  3) run zhsnap.py
  4) press space to take a photo (to modify edit PHOTO_KEY)
  5) quitting
     a) to only save the jpg files press w (to modify edit QUIT_IMG_MODE_KEY)
     b) to create ZIP and PDF press q (to modify edit QUIT_KEY)
"""

import cv2, os, shutil, sys
from fpdf import FPDF

FILENAME = "zh_NEPTUNCODE"
WEBCAM_PATH = "http://192.168.0.213:8080/video" #using IP Webcam app
QUIT_KEY = 'q'
QUIT_IMG_MODE_KEY = 'w'
PHOTO_KEY = ' '

cam = cv2.VideoCapture(WEBCAM_PATH)
cam.set(cv2.CAP_PROP_BUFFERSIZE, 0)
cv2.namedWindow("capture")

if not cam.isOpened():
    print("Cannot open camera")
    sys.exit()

imgid = 1
img_names = []

while True:
    ret, frame = cam.read()

    if not ret:
        print("Can't receive frame")
        break

    cv2.imshow("capture", frame)

    key = cv2.waitKey(1)

    if key == ord(QUIT_KEY):
        break
        
    if key == ord(QUIT_IMG_MODE_KEY):
        cv2.destroyAllWindows()
        sys.exit()

    if key == ord(PHOTO_KEY):
        img_name = "{}.jpg".format(imgid)
        cv2.imwrite(img_name, frame)
        print(img_name + " written")
        img_names.append(img_name)
        imgid += 1
        

cv2.destroyAllWindows()

dirname = FILENAME
os.mkdir(dirname)
pdf = FPDF()
pdf.set_auto_page_break(0)

for i in img_names:
    pdf.add_page()
    pdf.image(i, w = 190)
    shutil.move(i, dirname)
    
pdf.output("{}.pdf".format(dirname), 'F')
shutil.make_archive(dirname, "zip", base_dir=dirname)
shutil.rmtree(dirname)
