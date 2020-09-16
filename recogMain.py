import model.easyocr.easyocr as easyocr
import sys
import os

if __name__ == '__main__':
    reader = easyocr.Reader(['en'])
    result = []
    picture_list = os.listdir(sys.argv[1])
    list1 = []
    for a in picture_list:
        if a.split('.')[1]=='jpg' or a.split('.')[1]=='png':
            list1.append(a)
    for a in list1:
        print(sys.argv[1]+'//'+a)
        result.append(reader.readtext(sys.argv[1]+'//'+a, detail=0))

    print(result)