import os

import cv2
import os
from random import choice

import youtube_dl

from crawler.settings import MEDIA_ROOT, PROXIES

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

    def _create_images(self, filepath):
        vidcap = cv2.VideoCapture(filepath)
        filename = os.path.basename(filepath)

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
                frame_filepath = os.path.join(settings.MEDIA_ROOT, f"frame-{filename}-{count}.jpg")
                cv2.imwrite(frame_filepath, image)
                frame_filepath_list.append(frame_filepath)
        return frame_filepath_list

    def _create_preview_video(self, frame_filepath_list, out_video_filepath):
        img_list = []
        if frame_filepath_list:
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

            for frame_filepath in frame_filepath_list:
                os.remove(frame_filepath)

#-----------------

class VideoDownloader:

    def download(self, url):
        filename = uuid.uuid4()
        #outname_pattern = str(filename) + '.%(ext)s'
        outname_pattern = str(filename) + '.mp4'
        out_filepath = os.path.join(MEDIA_ROOT, outname_pattern)
        self.ydl_opts = {
            'outtmpl': out_filepath
        }
        if PROXIES:
            proxy = choice(PROXIES)
            self.ydl_opts['proxy'] = proxy

        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])

        return out_filepath, outname_pattern



