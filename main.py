import numpy as np
import cv2

def main():
    print("Hallo")
    img = cv2.imread('/Users/Bjoern/Data/pythonWS/FarmWatchPython/bin/MFDC8948.JPG')
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()