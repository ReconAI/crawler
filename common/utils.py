import os

import cv2
import os

import youtube_dl

from crawler.settings import MEDIA_ROOT

import uuid
from django.core.files.storage import default_storage
from django.core.files import File
from django.conf import settings

class PreviewDispatcher:

    def make_video(self, video_filepath):
        preview_filename = "%s_preview.ogg" % os.path.basename(video_filepath)
        preview_filepath = os.path.join(settings.MEDIA_ROOT, preview_filename)

        frame_filepath_list = self._create_images(video_filepath)
        self._create_preview_video(frame_filepath_list, preview_filepath)
        return preview_filepath, preview_filename

    def _create_images(self, filename):
        vidcap = cv2.VideoCapture(filename)

        fps = vidcap.get(cv2.CAP_PROP_FPS)
        frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps if fps > 0 else 0

        main_step = 10000  # miliseconds
        second_step = 100
        iteration_count = int(duration / 10) - 1

        count = 0
        frame_filepath_list = []
        for iteration in range(1, iteration_count + 1):
            for frame_index in range(1, 10 + 1):
                position = main_step * iteration + second_step * frame_index
                vidcap.set(cv2.CAP_PROP_POS_MSEC, position)
                success, image = vidcap.read()
                print('Read a new frame: ', success)
                count += 1
                frame_filepath = os.path.join(settings.MEDIA_ROOT, "frame%d.jpg" % count)
                cv2.imwrite(frame_filepath, image)
                frame_filepath_list.append(frame_filepath)
        return frame_filepath_list

    def _create_preview_video(self, frame_filepath_list, out_video_filepath):
        img_list = []
        for frame_filepath in frame_filepath_list:
            img = cv2.imread(frame_filepath)
            height, width, layers = img.shape
            size = (width, height)
            img_list.append(img)

        fps = 10
        #out_video_filepath=os.path.join(settings.MEDIA_ROOT, video_filename)
        out = cv2.VideoWriter(out_video_filepath, cv2.VideoWriter_fourcc(*'VP80'), fps, size)

        print(len(img_list))
        for i in range(len(img_list)):
            out.write(img_list[i])
        out.release()

#-----------------

class VideoDownloader:

    def download(self, url):
        filename = uuid.uuid4()
        #outname_pattern = str(filename) + '.%(ext)s'
        outname_pattern = str(filename) + '.mp4'
        out_filepath = os.path.join(MEDIA_ROOT, outname_pattern)
        self.ydl_opts = {
            # 'proxy': 'http://QWtbaCjOgK:UJQv1Nzdz7@45.140.174.102:55867',
            # 'proxy': 'http://192.168.88.245:30128',
            'outtmpl': out_filepath
        }
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            # ydl.download(['https://vimeo.com/whitehousepost/cats-in-tanks'])
            # ydl.download(['https://www.youtube.com/watch?v=WEkSYw3o5is'])
            ydl.download([url])


        # s3_file = default_storage.open(outname_pattern, 'w')
        # with open(out_filepath, 'rb') as f:
        #     b_content = f.read()
        #     s3_file.write(b_content)
        #     s3_file.close()
        # return s3_file.url
        return out_filepath, outname_pattern



