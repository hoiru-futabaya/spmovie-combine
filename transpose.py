#!/usr/bin/python
# coding: utf8
import ffmpeg
import os

path = '001.mp4'

#os.chmod(path, 0777)

input = ffmpeg.input(path)

audio = input.audio

PAD_OPTIONS={'width':'2000','height':'2000','padright':'606','padleft':'606','color':'Black'}
input = input.filter('transpose', 1)
input = input.filter('scale', 608, -1)
#input = input.filter('pad',PAD_OPTIONS)

out =ffmpeg.output(input, audio, 'test.mp4')

ffmpeg.run(out)
