class Path:
    def __init__(self, _os):
        if _os == 'win':
            self.path = 'C:/Users/jerry/PycharmProjects/auto_video_label'
        elif _os == 'ubuntu':
            self.path = '/home/jerry/Documents/workspaces/auto_video_label/src/video_feed_process'
        self.folder = _Folder(self.path)
        self.file = _File(self.path)


class _Folder:
    def __init__(self, path):
        self.raw_images = path + '/raw_images'
        self.parsed_images = path + '/parsed_images'


class _File:
    def __init__(self, path):
        self.sample = path + '/videos/sample.MOV'
        self.calibration = path + '/videos/calib.MOV'
        self.grab_data = path + '/temp_grab_data.txt'


class GrabTimer:
    def __init__(self):
        self._grab_frames = list()
        self._release_frames = list()

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
