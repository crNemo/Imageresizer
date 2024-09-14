import cv2

imgsrc=input("Enter the name of image or source: ")
new_imgsrc=input("Enter the new name of image or source with extension: ")
scale=int(input("Enter by what percent you want to resize (In percentage): "))
img=cv2.imread(f"{imgsrc}", cv2.IMREAD_UNCHANGED)

new_width=int(img.shape[1]*scale/100)
new_height=int(img.shape[0]*scale/100)

new_img=cv2.resize(img,(new_width,new_height))
cv2.imwrite(f"{new_imgsrc}", new_img)