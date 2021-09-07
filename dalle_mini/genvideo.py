# Loading all the packages required
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
from moviepy import editor

'''
Creating class MP3ToMP4 which contains methods to convert
an audio to a video using a list of images.
'''


class MP3ToMP4:

    def __init__(self, folder_path, audio_path, video_path_name):
        """
        :param folder_path: contains the path of the root folder.
        :param audio_path: contains the path of the audio (mp3 file).
        :param video_path_name: contains the path where the created
                                video will be saved along with the
                                name of the created video.
        """
        self.folder_path = folder_path
        self.audio_path = audio_path
        self.video_path_name = video_path_name

        # Calling the create_video() method.
        self.create_video()

    def get_length(self):
        """
        This method reads an MP3 file and calculates its length
        in seconds.

        :return: length of the MP3 file
        """
        song = MP3(self.audio_path)
        return int(song.info.length)

    def get_images(self):
        """
        This method reads the filenames of the images present
        in the folder_path of type '.png' and stores it in the
        'images' list.

        Then it opens the images, resizes them and appends them
        to another list, 'image_list'

        :return: list of opened images
        """
        path_images = Path(self.folder_path)
        images = list(path_images.glob('*.png'))
        image_list = list()
        for image_name in images:
            image = Image.open(image_name).resize((800, 800), Image.ANTIALIAS)
            image_list.append(image)
        return image_list

    def create_video(self):
        """
        This method calls the get_length() and get_images()
        methods internally. It then calculates the duration
        of each frame. After that, it saves all the opened images
        as a gif using the save() method. Finally it calls the
        combine_method()

        :return: None
        """
        length_audio = self.get_length()
        image_list = self.get_images()
        duration = int(length_audio / len(image_list)) * 1000
        image_list[0].save(self.folder_path + "temp.gif",
                           save_all=True,
                           append_images=image_list[1:],
                           duration=duration)

        # Calling the combine_audio() method.
        self.combine_audio()

    def combine_audio(self):
        """
        This method attaches the audio to the gif file created.
        It opens the gif file and mp3 file and then uses
        set_audio() method to attach the audio. Finally, it
        saves the video to the specified video_path_name

        :return: None
        """
        video = editor.VideoFileClip(self.folder_path + "temp.gif")
        audio = editor.AudioFileClip(self.audio_path)
        final_video = video.set_audio(audio)
        final_video.write_videofile(self.video_path_name, fps=60)