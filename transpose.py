#!/usr/bin/python
# coding: utf8
import ffmpeg
import os

path = '001.mp4'

#os.chmod(path, 0777)

input = ffmpeg.input(path)

audio = input.audio

info = ffmpeg.probe(path)

video_info = next((stream for stream in info['streams'] if stream['codec_type'] == 'video'), None)

w = video_info['width']
h = video_info['height']
r = video_info['tags']['rotate']

print(str(w) + ',' + str(h) + ',' + str(r))

x = w / 9 * 16

a = x - h 

input = input.filter('transpose', 1)
input = input.filter('pad', 0, x, 0, a/2, 'black')
input = input.filter('scale', -1, 1920)

out =ffmpeg.output(input, audio, 'test.mp4')

ffmpeg.run(out, overwrite_output=True)
