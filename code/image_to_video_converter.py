import cv2
import os


def images_to_video(path):
    img_array = []

    imgList = os.listdir(path)
    # imgList.sort(key=lambda x: int(x.split('.')[0]))
    for count in range(0, len(imgList)):
        filename = imgList[count]
        print(filename)
        img = cv2.imread(path + filename)
        if img is None:
            print(filename + " is error!")
            continue
        img_array.append(img)

    height, width, layers = img.shape
    size = (width, height)
    fps = 2.5
    out = cv2.VideoWriter('data_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


def main():
    path = "./data collection/mudd 2nd floor1/"
    images_to_video(path)


if __name__ == "__main__":
    main()