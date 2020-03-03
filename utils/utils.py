class Path:
    def __init__(self, _os, _type):
        if _os == 'win':
            self.path = 'C:/Users/jerry/PycharmProjects/auto_video_label'
        elif _os == 'ubuntu':
            self.path = '/home/jerry/Documents/workspaces/auto_video_label/src/video_feed_process'
        self.folder = _Folder(self.path)
        self.file = _File(self.path, _type)


class _Folder:
    def __init__(self, path):
        self.raw_images = path + '/raw_images'
        self.parsed_images = path + '/parsed_images'


class _File:
    def __init__(self, path, _type):
        self.sample = path + '/videos/sample' + _type
        self.calibration = path + '/videos/calib' + _type
        self.grab_data = path + '/grab_data.txt'


class GrabTimer:
    def __init__(self, grab_data):
        self._grab_frames = list()
        self._release_frames = list()
        self._grab_data = grab_data

    def set_grab_frames(self, num):
        if num <= 0:
            raise ValueError
        self._grab_frames.append(num)
        return 0

    def set_release_frames(self, num):
        if num <= 0:
            raise ValueError
        self._release_frames.append(num)
        return 0

    def get_grab(self):
        return self._grab_frames.pop()

    def get_release(self):
        return self._release_frames.pop()

    def find_cluster(self):
        grab_data_txt = open(self._grab_data)
        prev_time = 0
        for line in grab_data_txt:
            if not prev_time:
                prev_time = int(line.split()[-1])
            current_time = int(line.split()[-1])

            if current_time > 1.1 * prev_time:
                pass
            else:
                prev_time = current_time


        grab_data_txt.close()
        return 0

    def time_to_frames(self):
        # 0147 is the end of green
        grab_data_txt = open(self._grab_data)
