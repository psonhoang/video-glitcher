from glitch_this import ImageGlitcher
import cv2
from numpy import random
import os
from os.path import isfile, join


glitcher = ImageGlitcher()
VID_FILEPATH = "./vid/stock-vid-1.mp4"
vidcap = cv2.VideoCapture(VID_FILEPATH)
fps = round(vidcap.get(cv2.CAP_PROP_FPS) / 60, 2)

# Get frame from video and save it as a jpeg
def getFrame(sec, count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        # save frame as JPG file
        cv2.imwrite("./temp/image"+str(count)+".jpg", image)
    return hasFrames

# Glitch each frame (jpg), save the glitched frame as a jpg, and 
# reassemble the glitched jpeg into a glitched video!
def processImagesToFrame():
    pathIn = './temp/'
    pathOut = 'output.mp4'
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    # for sorting the file names properly
    files.sort(key=lambda x: x[5:-4])
    files.sort()
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    # for sorting the file names properly
    files.sort(key=lambda x: x[5:-4])
    for i in range(len(files)):
        filename = pathIn + files[i]
        intensity = random.randint(2, 10)
        # glitched image (frame as image) - glitch intensity is random!
        glitched_img = glitcher.glitch_image(
            filename, intensity, color_offset=True, scan_lines=True)
        # save glitched frame as image
        glitched_img.save(f"./glitched_frames/glitched{i+1}.jpg")
        # open glitched frame as an image
        img = cv2.imread(f"./glitched_frames/glitched{i+1}.jpg")
        height, width, layers = img.shape
        size = (width, height)
        #inserting the glitched frame into the frame array
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut, 0x7634706d, fps, size)
    for i in range(len(frame_array)):
        # writing to the frame array
        out.write(frame_array[i])
    out.release()
    return


if __name__ == '__main__':
    # Split video frames into images
    sec = 0
    count = 1
    success = getFrame(sec, count)
    while success:
        count = count + 1
        sec = sec + fps
        sec = round(sec, 2)
        success = getFrame(sec, count)

    # Release everything when the job is finished
    vidcap.release()
    cv2.destroyAllWindows()

    # Process each image and convert them back into frames to assemble
    # glitched video
    processImagesToFrame()