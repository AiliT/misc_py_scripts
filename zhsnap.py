"""
ZHSnap - automatically create PDF and ZIP files out of photos taken.
Modules installed with pip: opencv-python, fpdf
WEBCAM_PATH can be modified to 0 to use system camera.
"""

import cv2, os, shutil, sys
from fpdf import FPDF

NEPTUN = "NEPTUNCODE"
WEBCAM_PATH = "http://192.168.0.213:8080/video" #using IP Webcam app
QUIT_KEY = 'q'
QUIT_IMG_MODE_KEY = 'w'
PHOTO_KEY = ' '

cam = cv2.VideoCapture(WEBCAM_PATH)
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

dirname = "zh_{}".format(NEPTUN)
os.mkdir(dirname)
pdf = FPDF()
pdf.set_auto_page_break(0)

for i in img_names:
    pdf.add_page()
    pdf.image(i)
    shutil.move(i, dirname)
    
pdf.output("{}.pdf".format(dirname), 'F')
shutil.make_archive(dirname, "zip", base_dir=dirname)
shutil.rmtree(dirname)
