#!/usr/bin/env python3

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

path = '/home/jerry/Documents/workspaces/auto_video_label/src/video_feed_process'
sample = path + '/sample.mp4'
image_array = list()
bridge = CvBridge()
fps = 30
video_length = 0


def get_images_from_video():
    global video_length, image_array
    try:
        video_cap = cv2.VideoCapture(sample)
        print('Parsing video')
    except cv2.error:
        print("Error: Failed to open file")
        return

    while video_cap.isOpened():
        ret, frame = video_cap.read()
        frame = bridge.cv2_to_imgmsg(frame, 'bgr8')
        if not ret:
            break
        image_array.append(frame)
        video_length += 1

    video_cap.release()
    print('Done parsing')


def publish_video_with_time_stamp(publisher, rate):
    i = 0
    while not rospy.is_shutdown():
        publisher.publish(image_array[i])
        i += 1
        i %= video_length
        rate.sleep()


def main():
    rospy.init_node('video_feed', anonymous=True)
    image_publisher = rospy.Publisher('/auto_label/raw_image_feed_timed', Image, queue_size=10)
    rate = rospy.Rate(fps)

    get_images_from_video()
    publish_video_with_time_stamp(image_publisher, rate)

    return 0


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print('End video presentation')
