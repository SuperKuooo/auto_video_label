import cv2
import numpy as np
from utils import utils, image

path = utils.Path('win')
grab_timer = utils.GrabTimer()
standard_size = 3000
video_length = 0


def get_images_from_video():
    global video_length
    try:
        video_cap = cv2.VideoCapture(path.file.sample)
    except cv2.error:
        print("Error: Failed to open file")
        return 1

    while video_cap.isOpened():
        ret, frame = video_cap.read()
        if not ret:
            break
        video_length += 1
        # Commenting out so it doesn't take two million years to save images
        # cv2.imwrite(path.folder.raw_images + '/{0:04d}.jpg'.format(video_length), frame)

    print('Done saving video.')
    print('Number of frames recorded: {}'.format(video_length))


def get_interested_images():
    global grab_timer
    grab_data_txt = open(path.file.grab_data)
    for line in grab_data_txt:
        if line[0] == '#':
            continue
        phrase = line.split()
        if phrase[0] == 'o':
            grab_timer.set_grab_frames(int(phrase[1]))
        elif phrase[0] == 'x':
            grab_timer.set_release_frames(int(phrase[1]))
    grab_data_txt.close()
    return 0


def image_process():
    start = grab_timer.get_grab() + 20
    end = grab_timer.get_release()
    image_set = image.ImageSet()

    for i in range(start, end):
        img = cv2.imread(path.folder.raw_images + '/{0:04d}.jpg'.format(i))
        image_set.evaluate_image(img)

    image_set.save_set(path)
    print('Done evaluating the set')


def main():
    # get_images_from_video()
    get_interested_images()
    image_process()
    return 0


if __name__ == '__main__':
    main()
