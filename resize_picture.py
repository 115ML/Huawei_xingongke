import cv2
import os
from time import *

def img_resize(image):
    height, width = image.shape[0], image.shape[1]
    # 设置新的图片分辨率框架
    width_new = 600
    height_new = 448
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
    return img_new

if __name__ == '__main__':
    time1 = time()
    path = "F:\\360MoveData\\Users\Lenovo\Desktop\huawei\\"
    pic_list = os.listdir(path)
    print(pic_list)
    for a in pic_list:
        if a.endswith('.jpg') or a.endswith('.png'):
            img = cv2.imread(path+a)
            print(path+a)
            img_new = img_resize(img)
            changdu = int(img_new.shape[0]/2)
            kuandu = int(img_new.shape[1]/2)
            dstImg = img[0:changdu, kuandu:img.shape[1]]
            cv2.imwrite('F:\\360MoveData\\Users\Lenovo\Desktop\huawei_temp\\qiege\\'+a, dstImg)
    time2 = time()
    print(time2-time1)
    cv2.waitKey(0)

