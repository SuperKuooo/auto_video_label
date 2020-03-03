import cv2
import numpy as np
from utils import utils, image

path = utils.Path('win', '.mp4')
grab_timer = utils.GrabTimer(path.file.grab_data)
standard_size = 3000
video_length = 0
fps = 30


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
        cv2.imwrite(path.folder.raw_images + '/{0:04d}.jpg'.format(video_length), frame)

    print('Done saving video.')
    print('Number of frames recorded: {}'.format(video_length))


def image_process():
    grab_timer.find_cluster()

    start = grab_timer.get_grab()
    end = grab_timer.get_release()

    image_set = image.ImageSet()

    for i in range(start, end):
        img = cv2.imread(path.folder.raw_images + '/{0:04d}.jpg'.format(i))
        image_set.evaluate_image(img)

    image_set.save_set(path)
    print('Done evaluating the set')


def main():
    # get_images_from_video()
    # get_interested_images()
    # image_process()
    return 0


if __name__ == '__main__':
    main()
