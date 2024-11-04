import cv2

imgsrc=input("Enter the source: ")
new_imgsrc=input("Enter the new name of image with extension: ")

new_width=int(input("Enter the new width: "))
new_height=int(input("Enter the new new height: "))

img=cv2.imread(f"{imgsrc}", cv2.IMREAD_UNCHANGED)

new_img=cv2.resize(img,(new_width,new_height))
cv2.imwrite(f"{new_imgsrc}", new_img)